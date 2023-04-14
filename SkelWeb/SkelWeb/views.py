from django.shortcuts import render

# Create your views here.
def homePage(request, *args, **kwargs):
    return render(request, 'home.html', {})