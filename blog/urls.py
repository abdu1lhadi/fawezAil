from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('customs/', views.customs, name='customs'),
    path('equtpment/', views.equtpment, name='equtpment'),
    path('heavy_haulage/', views.heavy_haulage, name='heavy_haulage'),
    path('jack_skidd/', views.jack_skidd, name='jack_skidd'),
    path('transport/', views.transport, name='transport'),
    path('job/', views.job, name='job'),
    path('listnews/', views.list_news, name='listnews'),
    path('warehouse/', views.warehouse, name='warehouse'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('clients/', views.clients, name='clients'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)