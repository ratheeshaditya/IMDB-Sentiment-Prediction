from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import nltk
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from nltk.corpus import stopwords
import re
#Initial start
nltk.download('stopwords')

MODEL = None
if MODEL is not None:
    pass
else:
    MODEL = load_model("model/model.h5")
    print("Model loaded")
    

tokenizer = None
if tokenizer is not None:
    pass
else:
    with open('model/tokenizer_imdb.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)
        print("Tokenizer loaded")
        print("Total no of words {}" .format(len(tokenizer.word_index)+1) )


def index(request):
    return render(request,"index.html")


def get_sentiment(request):
    if request.method=='POST':
        text_sentiment = request.POST['review']
        get_sentiment = make_sentiment(text_sentiment)
        if get_sentiment==1:
            image_load = "Positive review"
        else:
            image_load = "Negative review"

        return render(request,"index.html",{'sentiment':image_load})


def make_sentiment(text) :
  #Convert string 
  process_text = text
  #Convert string to lower
  process_text = process_text.lower()
#   #Removing html tags
  process_text = re.sub("<.*?>"," ",process_text)
#   #Removing all digits and having only letters
  process_text = re.sub("[^a-zA-Z]"," ",process_text)
#   #Removing all stop words
  process_text = process_text.split(" ")
  process_text = " ".join([word for word in process_text if word not in stopwords.words("english")])

  make_sequence = tokenizer.texts_to_sequences([process_text])
  non_array_sequence = tokenizer.texts_to_sequences(process_text)
  make_sequence = pad_sequences(make_sequence,padding="post")
  predict_class = MODEL.predict_classes(make_sequence)

  return predict_class