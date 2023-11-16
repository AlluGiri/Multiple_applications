from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MSD(request):
    return render(request,'MSD.html')

def raina(request):
    return HttpResponse('<h1>Raina Here:The first Indian batsman to hit a century in all three formats of international cricket.<h1>')