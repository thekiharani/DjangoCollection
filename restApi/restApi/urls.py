from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from languages import views as lang_views
# from soccer import  views as soccer_views

# router = routers.DefaultRouter()

# router.register('languages', lang_views.LanguageView)
# router.register('paradigms', lang_views.ParadigmView)
# router.register('programmers', lang_views.ProgrammerView)

# router.register('pizzas', soccer_views.PizzaView)
# router.register('orders', soccer_views.OrderView)
# router.register('ordermeta', soccer_views.OrderMetaView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/dev/', include('languages.urls')),
    path('api/soccer/', include('soccer.urls')),
    # path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
