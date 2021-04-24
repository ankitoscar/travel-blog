from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('page-2/', views.page_2, name='page-2'),
    path('page-3/', views.page_3, name='page-3'),
]