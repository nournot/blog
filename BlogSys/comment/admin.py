from django.contrib import admin

# Register your models here.
from .models import Comment
from BlogSys.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['target', 'nickname', 'website', 'email', 'status',
                    'created_time']
    fields = ['target', 'nickname', ('website', 'email'), 'status', 'content']


