from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('student', views.IndexView.as_view(), name = 'index'),
]