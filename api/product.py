from django.shortcuts import render
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes



@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        category_id = request.GET.get('category')  #?category=...
        if category_id:
            if not Category.objects.filter(id=category_id).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Product created successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk = None):
    try:
        product = Product.objects.get(id=pk)
    except:
        return Response("Product id error", status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Product updated successfully", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        if not request.user.is_staff:
            return Response(status=status.HTTP_403_FORBIDDEN)
        product.delete()
        return Response("Product deleted successfully", status=status.HTTP_204_NO_CONTENT)


#
#
