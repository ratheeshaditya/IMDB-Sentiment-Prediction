# IMDB-Sentiment-Prediction
A ML Integrated Django application to predict the sentiment of the text trained on the IMDB dataset.

The notebook for the creation of the model can be found here : https://github.com/ratheeshaditya/NLP/blob/main/IMDB_Sentiment_Analysis.ipynb

Instructions 
- Run 'python manage.py collectstatic' on the first run

- To run server : python manage.py runserver

- In the model folder there is only 'tokenizer' file , To use the weights : https://gofile.io/d/lg06CH and store it in the model folder itself.

- The main 'views.py' is in the sentiment folder where all the text preprocessing and prediction of the sentiment is done.

<h2>Positive review</h2>
<img src="https://user-images.githubusercontent.com/15837342/96734934-b3bd2500-13c3-11eb-8123-5cb2a04e2298.gif" height="500" width="500">

<h2>Negative review</h2>
<img src="https://user-images.githubusercontent.com/15837342/96735656-760ccc00-13c4-11eb-9449-5220f3179a79.gif" height="500" width="500">
