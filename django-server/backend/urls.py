from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.say_hello),
    path('sentiment/', views.sentiment_analysis),
    path('emotion/', views.emotion_analysis),
    path('stocks/', views.stock_predict),
    path('three/', views.all_three)
]