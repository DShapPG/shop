from django.urls import path
from api import product, categories
from api import users
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("products", product.product_list),
    path("products/<int:pk>", product.product_detail),
    path("users/register", users.create_user),
    path("users/<int:pk>", users.user_detail),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("categories", categories.get_categories),

]
