from django.shortcuts import render, HttpResponse
from django import http
from .models import *


# Create your views here.
def slide_list(request):
    data = {
        'meta': {},
        'objects': []
    }
    res = Slider.objects.filter(is_valid=1)
    for i in res:
        data['objects'].append(
            {
                'id': i.id,
                'name': i.name,
                'img_url': i.img.url,
                'target_url': i.target_url
            }
        )

    return http.JsonResponse(data)
