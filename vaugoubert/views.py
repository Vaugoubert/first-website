from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def home_page2(request):
    return render(request, 'home_page2.html', {})

def chateau(request):
    return render(request, 'chateau.html', {})

def boulot(request):
    return render(request, 'boulot.html', {})

def repos(request):
    return render(request, 'repos.html', {})

def histoire(request):
    return render(request, 'histoire.html', {})

def detente(request):
    return render(request, 'detente.html', {})