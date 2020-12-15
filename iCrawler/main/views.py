from uuid import uuid4
from urllib.parse import urlparse
from django.core.validators import URLValidator
from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from time import sleep
import os
import json

import requests
        

def is_valid_url(url):
    validate = URLValidator()
    try:
        validate(url) # check if url format is valid
    except ValidationError:
        return False

    return True

@csrf_exempt
@api_view(['POST',])
def getProduct(request):

    url = request.POST['url']

    if not url:
        return JsonResponse({'error': 'Missing  args'})
        
    if not is_valid_url(url):
        return JsonResponse({'error': 'URL is invalid'})

    data = {
        "request": {
            "url": str(url),
            "callback": "start_requests",
            "dont_filter": "true"
        },
        "spider_name": "GetinfoSpider"
    }

    scrapyrt = 'http://127.0.0.1:9080/crawl.json'

    try:
        response = requests.post(scrapyrt, json = data)
        r = response.json()
        return JsonResponse({'data': r})
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)})

@csrf_exempt
@api_view(['POST',])
def getVariations(request):

    url = request.POST['url']

    if not url:
        return JsonResponse({'error': 'Missing  args'})
        
    if not is_valid_url(url):
        return JsonResponse({'error': 'URL is invalid'})

    data = {
        "request": {
            "url": str(url),
            "callback": "start_requests",
            "dont_filter": "true"
        },
        "spider_name": "GetVariationsSpider"
    }

    scrapyrt = 'http://127.0.0.1:9080/crawl.json'

    try:
        response = requests.post(scrapyrt, json = data)
        r = response.json()
        return JsonResponse({'data': r})
    except Exception as e:
        print(e)
        return JsonResponse({'error': str(e)})


    