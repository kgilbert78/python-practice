from django.shortcuts import render, HttpResponse

# Create your views here.

def Index(request): #step-1
    return HttpResponse("Index displays here.") # and import HttpResponse above
