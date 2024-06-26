
from django.urls import path
from . import views

urlpatterns = [
    #path('home', views.home),
    path('', views.HomeView.as_view()),
    #path('authorized', views.authorized),
    path('authorized', views.AuthorizedView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
