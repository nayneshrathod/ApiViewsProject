from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import response


# Create your views here.
def index(request):
    data = {"name":"Naynesh"}
    return HttpResponse(data)
