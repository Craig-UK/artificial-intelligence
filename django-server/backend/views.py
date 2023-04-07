from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def say_hello(request):
    body = json.loads(request.body)
    print(body["value"])
    return JsonResponse({'result': body["value"]})