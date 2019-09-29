from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from store.models import Product


@api_view(['GET'])
def view_prouct(request):
    products = Product.objects.all()
    results = [product.to_json() for product in products]
    return Response(results, status = status.HTTP_200_OK)


# Create your views here.
