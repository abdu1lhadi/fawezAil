from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)