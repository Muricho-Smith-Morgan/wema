from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('causes', views.causes, name='causes'),
    path('event', views.event, name='event'),
    path('blog', views.blog, name='blog'),
    path('single', views.single, name='single'),
    path('service', views.service, name='service'),
    path('team', views.team, name='team'),
    path('donate', views.donate, name='donate'),
    path('donate_now/<str:pk>', views.donate_now, name='donate_now'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('contact', views.contact, name='contact'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('register', views.register, name='register'),
    path('panel', views.panel, name='panel'),
    path('admin', views.admin, name='admin'),
    path('response', views.response, name='response'),
]