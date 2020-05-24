from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from cart.views import export

urlpatterns = [
    path('', export),
    path('admin/', admin.site.urls),
    path('api/dev/', include('languages.urls')),
    path('api/soccer/', include('soccer.urls')),
    path('api/cart/', include('cart.urls')),
    # path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
