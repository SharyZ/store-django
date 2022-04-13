from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category
from .serializers import CategorySerializer

# Create your views here.


@api_view(['GET'])
def categoriesList(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def categoriesDetail(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)
    except Category.DoesNotExist:
        return Response({ 'error': 'category not found' }, status=status.HTTP_404_NOT_FOUND)
