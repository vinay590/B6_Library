from django.contrib import admin
from .models import Book,Post
# Register your models here.
print("in admin.py")
admin.site.register(Book)
admin.site.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'desc' ,'publish']
