from django.urls import path

from . import views
from .views import TestCreate, znacky

urlpatterns = [
    path('', views.index, name='index'),
    path('odpoved-create', TestCreate.as_view(), name='odpoved-create'),
    path('statistiky', views.stat, name='stat'),
    path('data', views.get_data, name='data'),
    path('znacky',views.znacky, name='znacky'),
]