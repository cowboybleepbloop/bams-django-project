from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.



def index(request):
    return render(request, 'flp_app/index.html', {'title': 'Home'} )

def disclaimer(request): 
    return render(request, 'flp_app/disclaimer.html', {'title': 'Disclaimer'})

def blog(request): 
    context = { 'posts': Post.objects.all()}
    
    return render(request, 'flp_app/blog.html', context)

    