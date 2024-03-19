from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')