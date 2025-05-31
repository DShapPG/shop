from django.shortcuts import render
from .models import Product, Category
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from rest_framework.decorators import api_view, permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('category', openapi.IN_QUERY, description="ID категории", type=openapi.TYPE_INTEGER),
        openapi.Parameter('search', openapi.IN_QUERY, description="Поиск по имени или описанию", type=openapi.TYPE_STRING),
        openapi.Parameter('price_min', openapi.IN_QUERY, description="Минимальная цена", type=openapi.TYPE_NUMBER),
        openapi.Parameter('price_max', openapi.IN_QUERY, description="Максимальная цена", type=openapi.TYPE_NUMBER),
    ],
    responses={200: ProductSerializer(many=True)}
)
@swagger_auto_schema(
    method='post',
    request_body=ProductSerializer,
    responses={201: openapi.Response("Product created successfully")}
)

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        category_id = request.GET.get('category')  #?category=...
        search = request.GET.get('search') # filter by name
        price_min = request.GET.get('price_min') # filter by price
        price_max = request.GET.get('price_max') # filter by price
        if category_id:
            if not Category.objects.filter(id=category_id).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            products = Product.objects.filter(category_id=category_id)
        if search:
            if not Product.objects.filter(name=search).exists() and not Product.objects.filter(description=search).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            if Product.objects.filter(name=search).exists():
                products = Product.objects.filter(name=search)
            elif Product.objects.filter(description=search).exists():
                products = Product.objects.filter(description=search)
        if price_min and price_max:
            if not Product.objects.filter(price__range=(price_min, price_max)).exists():
                return Response(status=status.HTTP_404_NOT_FOUND)
            products = Product.objects.filter(price__range=(price_min, price_max))
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
