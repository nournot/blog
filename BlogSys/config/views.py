from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import Link
from blog.views import CommonViewMixin


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL).order_by('-weight')
    template_name = 'config/links.html'
    context_object_name = 'link_list'

# def links(request):
#     links = Link.objects.filter(status=Link.STATUS_NORMAL)
#     context = {
#         'links':links
#     }
#     return render(request, template_name='config/links.html' , context=context)