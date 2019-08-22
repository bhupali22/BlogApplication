from .models import Post

def blogs_count(request):
    blog_count = Post.objects.count()
    return {"blog_count" : blog_count}