from api.models import Cart
from api.serializer import CartSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_cart(request):
    if request.method == 'GET':
        cart_items = Cart.objects.all()
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        cart = create_cart(request)
        if cart.status_code == status.HTTP_201_CREATED:
            return add_product(request)
        return cart


def create_cart(request):
    try:
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def add_product(request):
    serializer = CartItemSerializer(data=request.data)
    cart = Cart.objects.get(user=request.user)
    if serializer.is_valid():
        serializer.save(cart=cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)