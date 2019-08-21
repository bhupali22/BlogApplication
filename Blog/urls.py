from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.displayBlog, name='displayBlog'),
    path('AddBlog/', views.add_blog, name ='AddBlogForm'),
]