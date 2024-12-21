from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('news/<slug:slug>/', views.article, name='article'),
    path('news/', views.news, name='news'),
    path('<slug:slug>/', views.page, name='page'),
    path('', views.index, name='index'),
    path('legs/<int:id>/', views.leg, name='leg')
]
