from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	re_path(r'^admin/',  admin.site.urls),
	re_path(r'auth/', include('knox.urls')),
    re_path(r'', include('dashboard.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)