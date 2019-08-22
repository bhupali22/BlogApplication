from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Post, Author
from .forms import AddBlog, SignupForm, SearchForm
# Create your views here.
def index(request):
    # if request.POST:
    #     if 'login_button' in request.POST:
    #         return render(request, 'registration/login.html')
    #     else:
    #         return render(request, 'registration/signup.html')
    # else:
    return render(request, 'Blog/index.html')

def displayBlog(request):
    post_obj = Post.objects.all()
    context = {
        'post_obj' : post_obj
    }
    return render(request, 'Blog/post.html', context)

def add_blog(request):
    context = {

    }
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddBlog(request.POST)
            if form.is_valid():
                try:
                    user1 = Author.objects.get(user = request.user)
                except:
                    user1 = Author.objects.create(user=request.user)

                new_post = Post.objects.create(
                    author = user1,
                    title = form.cleaned_data.get('title'),
                    description = form.cleaned_data.get('description'),
                    publish_date = timezone.now()
                )
                new_post.save()
                return redirect('displayBlog')
        else:
            form1 = AddBlog()
            context['form'] = form1

    return render(request,'Blog/ShowForm.html',context)


def signUp(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('displayBlog')
    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form' : form})

def search_blog(request):
    context = {

    }
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            context['title'] = title
            post_obj = Post.objects.filter(title__icontains = title)
            context['post_obj'] = post_obj
            #return HttpResponse("title : %s" % post_obj)
    else:
        context['form'] = SearchForm()
    return render(request, 'Blog/searchForm.html', context)