from django.urls import path

from . import views


urlpatterns =[
path("",views.index,name="index"),
path("get_sentiment",views.get_sentiment,name="get_sentiment")
]
