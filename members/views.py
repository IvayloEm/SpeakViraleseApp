from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're in the member zone.")


def writer_view(request):
    return render(request, 'members/writer-view.html')

