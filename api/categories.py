from .models import Category
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .serializer import CategorySerializer


@api_view(['GET', 'POST'])
def get_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_staff:
            return Response(status = status.HTTP_403_FORBIDDEN)
        category = Category.objects.create(name=request.data)
        return Response("Category created successfully", status=status.HTTP_201_CREATED)