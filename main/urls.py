from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:slug>/', views.post, name='post'),
]
