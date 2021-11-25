from django.conf.urls import url
from django.conf.urls.static import static

from project import settings
from . import views

app_name = 'chat'

urlpatterns = [
    url('', views.chat_view, name='chat_view'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
