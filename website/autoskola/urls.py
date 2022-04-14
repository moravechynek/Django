from django.urls import path

from . import views
from .views import TestCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('odpoved-create', TestCreate.as_view(), name='odpoved-create')
]