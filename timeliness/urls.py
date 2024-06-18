from django.urls import path
from . import views


urlpatterns = [
    path('', views.timeliness, name='timeliness')
    ]