from django.shortcuts import render
from django.utils import timezone

from .models import Post, Author
from .forms import AddBlog
# Create your views here.
def index(request):
    if request.POST:
        if 'login_button' in request.POST:
            return render(request, 'registration/login.html')
        else:
            return render(request, 'registration/register.html')
    else:
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
                #user1 = Author.objects.get(user = request.user)
                user1 = Author.objects.create(user=request.user)
                new_post = Post.objects.create(
                    author = user1,
                    title = form.cleaned_data.get('title'),
                    description = form.cleaned_data.get('description'),
                    publish_date = timezone.now()
                )
                new_post.save()
        else:
            form1 = AddBlog()
            context['form'] = form1

    return render(request,'Blog/ShowForm.html',context)


