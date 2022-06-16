# Django
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

# Django Rest Framework
from rest_framework.response import Response
from rest_framework.decorators import api_view

# models
from products.models import Product

# serializer
from products.serializers import ProductSerializer

# utils
import json


def classic_django_api_home(request, *args, **kargs):
    model_data = Product.objects.all().first()
    data = {}
    """
    The DRF functionality made with Django
    
    if request.method != "POST":
        return Response({"detail": "GET not allowed"}, status=405)
        
    """
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
        # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type":"application/json"})
    return JsonResponse(data)


@api_view(["GET"])
def drf_api_home(request, *args, **kargs):
    data = request.data
    instance = Product.objects.all().first()
    data = {}
    if instance:
        #data = model_to_dict(instance, fields=['id', 'title'])
        data = ProductSerializer(instance).data
    return Response(data)


@api_view(["POST"])
def drf_api_post(request, *args, **kargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        #print(instance)

        print(serializer.data)
        return Response(serializer.data)
    else:
        return Response({'invalid': 'not good data'}, status=400)
