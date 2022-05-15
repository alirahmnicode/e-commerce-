from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("product.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    path("user/", include("users.urls")),
    path("api/", include("api.urls")),
    path("auth/", include("djoser.urls")),
    path('auth/',include('djoser.urls.jwt')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
