from django.shortcuts import render

# Create your views here.

def virat(request):
    return render(request,'rcb.html')

def msd(request):
    return render(request,'csk.html')