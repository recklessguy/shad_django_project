
from django.contrib import admin
from django.urls import path, include
from django.conf import Settings, settings
from django.conf.urls.static import static

urlpatterns = [
    path('traufter/', admin.site.urls),
    path('', include('shabd.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

