from django.urls import path 
from django.conf.urls import include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('accounts/', include("django.contrib.auth.urls"))
]