from django.contrib import admin
from django.urls import include, path

from ApiViewsApp import views

urlpatterns = [
    path('', views.index,name = "Home"),
]
