from django.contrib import admin
from .models import Post

# 定义Post显示方式的类
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post,PostAdmin)