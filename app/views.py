from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    weather=None
    if request.method=='POST':
        city=request.POST['city']
        weather=requests.get(f'https://goweather.herokuapp.com/weather/{city}').json()
        weather['city'] = city.title()
    return render(request,'index.html',{'weather':weather})