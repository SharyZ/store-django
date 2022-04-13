from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

# Create your views here.


@api_view(['GET'])
def cartItemsList(request):
    cart_items = CartItem.objects.all()
    serializer = CartItemSerializer(cart_items, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def cartItemUpdate(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        serializer = CartItemSerializer(instance=cart_item, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({ 'error': 'cart item not found' }, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def cartItemDelete(request, cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({ 'error': 'cart item not found' }, status=status.HTTP_404_NOT_FOUND)
