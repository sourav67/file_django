from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/' ,  views.post_list, name='post_list'),
    path('files/' ,  views.files_list, name='files_list'),
    path('files/upload/' ,views.upload_file, name='upload_file')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
