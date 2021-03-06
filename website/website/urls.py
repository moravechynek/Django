from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('autoskola/', include('autoskola.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='autoskola/')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)