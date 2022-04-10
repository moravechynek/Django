from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('autoskola/', include('autoskola.urls')),
    path('admin/', admin.site.urls),
]