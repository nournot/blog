from django.contrib import admin

# Register your models here.
from .models import Link, SideBar
from BlogSys.custom_site import custom_site
from BlogSys.BaseOnwerAdmin import BaseOwnerAdmin


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'href', 'weight', 'status', 'created_time', 'owner']
    fields = ['title', 'href', 'weight', 'status']

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(LinkAdmin, self).save_model(request, obj, form, change)


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'status', 'owner', 'created_time']
    fields = ['title', 'display_type', 'status', 'content']

    # def save_model(self, request, obj, form, change):
    #     obj.owner = request.user
    #     return super(SideBar, self).save_model(request, obj, form, change)