
from django.contrib import admin

from .models import BlogPost, Comment


@admin.register(Comment)   # az in rah ham mishe ke beghesh decoraitor migan
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'datetime_created', 'is_active']


admin.site.register(BlogPost)
