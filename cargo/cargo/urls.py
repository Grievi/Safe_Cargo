from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views

router=routers.DefaultRouter()
router.register(r'profile', views.ProfileApi)
router.register(r'cargo', views.CargoApi)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include(router.urls)),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]
