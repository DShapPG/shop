from api import product, categories, users, cart
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, re_path

schema_view = get_schema_view(
    openapi.Info(
        title="Название API",
        default_version='v1',
        description="Описание вашего API",
        contact=openapi.Contact(email="your@email.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("products/", product.product_list),
    path("products/<int:pk>", product.product_detail),
    path("users/register", users.create_user),
    path("users/<int:pk>", users.user_detail),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("categories", categories.get_categories),
    path("cart/", cart.get_cart),
# Swagger UI:
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
