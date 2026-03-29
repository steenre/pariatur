from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.siteManager, name='site-manager'),
    path('logout/', views.quitSiteManager, name='logout-site-manager'),
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create, name='create'),
    path('create-category/', views.createCategory, name='create-category'),
    path('manage/', views.manage, name='manage'),
    path('edit/<slug:slug>', views.edit, name='edit'),
    path('edit-category/<str:cat_name>', views.editCategory, name='edit-category'),
    path('remove/<slug:slug>', views.remove, name='remove'),
    path('remove-category/<str:cat_name>', views.removeCategory, name='remove-category'),
    # path('/', views., name=''),
]
