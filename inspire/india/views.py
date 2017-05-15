from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
 return HttpResponse("<h2>Inspire Techno Park LLP, Tuticorin, India -628 001.</h2>")
