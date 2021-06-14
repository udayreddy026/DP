from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    context = {
        'posts_1': Post.objects.all(),
        'title':'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})