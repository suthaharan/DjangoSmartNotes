
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:pk>', views.detail)
]
