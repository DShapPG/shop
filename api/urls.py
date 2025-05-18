from django.urls import path
from api import product
from api import users

urlpatterns = [
    path("products", product.product_list),
    path("products/<int:pk>", product.product_detail),
    path("users/register", users.create_user),
    path("users/<int:pk>", users.user_detail)
]
