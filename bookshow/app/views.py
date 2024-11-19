from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def index1(req):
    return render(req,'index1.html')
