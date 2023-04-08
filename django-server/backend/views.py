from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sentiment import Sentiment
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
