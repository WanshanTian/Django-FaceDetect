from django.urls import path
from .views import detect
from FaceDetect import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', detect, name='oripage')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)