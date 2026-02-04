import json
from django.shortcuts import render
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # byte string of json data
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    return JsonResponse({"message": "Hi there, this is django api response"})