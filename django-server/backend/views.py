from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sentiment import Sentiment
from .emotion import GetEmotion
from .stockpredict import Predict
from .converter import Convert
from numpy.random import seed
from numpy.random import randint

seed(50)

# Create your views here.
@csrf_exempt
def say_hello(request):
    body = json.loads(request.body)
    print(body["value"])
    return JsonResponse({'result': body["value"]})

@csrf_exempt
def sentiment_analysis(request):
    body = json.loads(request.body)
    print(body["value"])
    sent = Sentiment(body["value"])

    arr = randint(0, 100, 15)
    print(list(arr))
    new_arr = [int(x) for x in arr]

    return JsonResponse({'result': sent, 'nums': new_arr})

@csrf_exempt
def emotion_analysis(request):
    body = json.loads(request.body)
    print(body["emValue"])
    em = GetEmotion(body["emValue"])

    return JsonResponse({'result': em})

@csrf_exempt
def stock_predict(request):
    body = json.loads(request.body)
    res = Predict(body["ticker"])
    if res == "Invalid Ticker":
        return JsonResponse({'result': "Failed"})
    else:
        original, preds = res
    return JsonResponse({'original': original, 'predictions': preds})

@csrf_exempt
def all_three(request):
    body = json.loads(request.body)
    Convert("short-video.mp4")
    emotion = GetEmotion("short-video.mp4")
    sent = Sentiment("PythonTesting3.wav")
    stocks = Predict(ticker=body["ticker"], emotion=emotion, sentiment=sent) #Should be a stock input and an input for the emotion and sentiment values
    if stocks == "Invalid Ticker":
        return JsonResponse({'result': 'Failed'})
    else:
        original, predictions = stocks
    return JsonResponse({'original': original, 'predictions': predictions, 'emotion': emotion, 'sentiment': sent})
