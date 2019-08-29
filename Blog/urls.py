from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    #path('', TemplateView.as_view(template_name = "Blog/index.html"), name='index'),      #when there is just need to render simple template the we can directly create TemplateView in URLconf. Any arguments passed to as_view() will override attributes set on the class.
    #path('post/', views.displayBlog, name='displayBlog'),                  #url for normal view : displayBlog(request)
    path('post/', views.displayBlog.as_view(), name = 'displayBlog'),       #url for displayBlog(View)

    path('post/<int:pk>/', views.BlogDetailView.as_view(), name = 'Blog_detail'),

    #path('AddBlog/', views.add_blog, name ='AddBlogForm'),
    path('delete/<int:pk>/', views.DeleteBlog.as_view(), name='delete_post'),
    path('AddBlog/', views.add_blog.as_view(), name ='AddBlogForm'),
    path('searchBlog/', views.search_blog, name='search_blog')
]