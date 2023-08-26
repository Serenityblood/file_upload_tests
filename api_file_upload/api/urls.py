from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import FileViewSet


app_name = 'api'


router_v1 = DefaultRouter()
router_v1.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('', include(router_v1.urls))
]
