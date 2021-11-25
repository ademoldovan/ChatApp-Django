
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'main'

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('chatApp/', include('chat.urls')),
    path('', views.homepage_view, name="homepage_view"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
