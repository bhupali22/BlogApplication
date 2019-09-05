from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View, TemplateView
from django.contrib.auth.decorators import login_required

from .models import Post, Author
from .forms import AddBlog, SearchForm, SignupForm


# Create your views here.
# def index(request):
#     # if request.POST:
#     #     if 'login_button' in request.POST:
#     #         return render(request, 'registration/login.html')
#     #     else:
#     #         return render(request, 'registration/signup.html')
#     # else:
#     return render(request, 'Blog/index.html')


class IndexView(TemplateView):
    template_name = 'Blog/index.html'

    def get_context_data(self, **kwargs):
        #context = super().get_context_data()       #This also works fine
        context = super(IndexView, self).get_context_data()        #whenever we need to pass some context, first we need to take context of super. while passing argument in super we need to provide IndexView name first and then self, otherwise it gives TypeError : super() argument 1 must be type, not IndexView
        context['name'] = 'Click to login or register'
        return context


# def displayBlog(request):                 #normal view
#     post_obj = Post.objects.all()
#     context = {
#         'post_obj' : post_obj
#     }
#     return render(request, 'Blog/post.html', context)


class displayBlog(ListView):
    #template_name = 'Blog/post.html'
    model = Post
    #queryset = Post.objects.all()
    #context_object_name = 'post_obj'
    #paginate_by = 2
    ordering = ['title']


# class displayBlog(View):
#     def get(self, request):
#         post_obj = Post.objects.all()
#         context = {
#             'post_obj' : post_obj
#         }
#         return render(request, 'Blog/post.html', context)





# def add_blog(request):
#     context = {
#
#     }
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AddBlog(request.POST)
#             #import ipdb;ipdb.set_trace()
#             print(form)
#             if form.is_valid():
#                 print("hello")
#                 try:
#                     user1 = Author.objects.get(user = request.user)
#                     #print(user1.first_name)
#                 except:
#                     user1 = Author.objects.create(user = request.user)
#                     # user1.save()
#                     #print(user1.first_name)
#
#                 #form.save()
#                 new_post = Post.objects.create(
#                     author = user1,
#                     title = form.cleaned_data.get('title'),
#                     description = form.cleaned_data.get('description'),
#                     publish_date = timezone.now()
#                 )
#                 new_post.save()
#                 return redirect('displayBlog')
#         else:
#             form1 = AddBlog()
#             #form1 = AddBlog(initial={'author': User.objects.get(id=request.user.id) })
#             #form = SellingForm(initial={'seller': Dealer.objects.get(id=request.user.id)})
#             context['form'] = form1
#
#     return render(request,'Blog/ShowForm.html',context)


# class add_blog(View):
#     def get(self, request):
#         form1 = AddBlog()
#         context = {'form' : form1}
#         return render(request, 'Blog/ShowForm.html', context)
#
#     def post(self, request):
#         if request.user.is_authenticated:
#             form = AddBlog(request.POST)
#             #import ipdb;ipdb.set_trace()
#             #print(form)
#             if form.is_valid():
#                 #print("hello")
#                 try:
#                     user1 = Author.objects.get(user = request.user)
#                     #print(user1.first_name)
#                 except:
#                     user1 = Author.objects.create(user = request.user)
#                     # user1.save()
#                     #print(user1.first_name)
#
#                 #form.save()
#                 new_post = Post.objects.create(
#                     author = user1,
#                     title = form.cleaned_data.get('title'),
#                     description = form.cleaned_data.get('description'),
#                     publish_date = timezone.now()
#                 )
#                 new_post.save()
#                 return redirect('displayBlog')

class DeleteBlog(DeleteView):
    template_name = 'Blog/blog_detail.html'
    success_url = reverse_lazy('displayBlog')
    model = Post

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


class add_blog(FormView):
    form_class = AddBlog
    template_name = 'Blog/ShowForm.html'
    success_url = reverse_lazy('displayBlog')

    def form_valid(self, form):
        # print("inside form_valid")
        try:
            # print("inside try")
            user1 = Author.objects.get(user = self.request.user)
            # print(user1.first_name)
        except:
            # print("inside except")
            user1 = Author.objects.create(user = self.request.user)
            # user1.save()
            # print(user1.first_name)

        # form.save()
        new_post = Post.objects.create(
            author=user1,
            title=form.cleaned_data.get('title'),
            description=form.cleaned_data.get('description'),
            publish_date=timezone.now()
        )
        new_post.save()
        return super(add_blog, self).form_valid(form)



class signUp(CreateView):
    form_class = SignupForm
    model = User
    # fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('displayBlog')
    #template_name = 'registration/signup.html'

    # def form_valid(self, form):     #Model form views provide a form_valid() implementation that saves the model automatically. You can override this if you have any special requirements;
    #     return super(signUp, self).form_valid(form)



class UpdatesignUp(UpdateView):
    form_class = SignupForm     #form_class and fields cannot be together
    model = User
    #fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('displayBlog')
    template_name = 'registration/signup.html'
    #fields = ('__all__')

    # def form_valid(self, form):
    #     return super(UpdatesignUp, self).form_valid(form)





# def signUp(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             return redirect('displayBlog')
#     else:
#         form = SignupForm()
#
#     return render(request, 'registration/signup.html', {'form' : form})


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


# class BlogDetailView(View):
#     def get(self, request,**kwargs):
#         blog = get_object_or_404(Post, id=kwargs['pk'])   #In a class-based view, all of the elements from the URL are placed into self.args (if they're non-named groups) or self.kwargs (for named groups). So, for your view, you can use self.kwargs['pk']
#         context = {'blog' : blog }
#         return render(request, 'Blog/blog_detail.html', context)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'Blog/blog_detail.html'
    #context_object_name = 'blog'
