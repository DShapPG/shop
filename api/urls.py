from django.urls import path
from api import product

urlpatterns = [
    path("products", product.product_list),
    path("products/<int:pk>", product.product_detail),

]
