from django.conf.urls.static import static
from django.urls import path
from galleryapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-image'),
    path('update/<int:image_id>', views.update_image),
    path('delete/<int:image_id>', views.delete_image)
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)