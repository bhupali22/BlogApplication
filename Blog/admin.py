from django.contrib import admin
from .models import Post, Author
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish_date',)



admin.site.register(Author)
admin.site.register(Post, PostAdmin)
