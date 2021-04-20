from django.shortcuts import render

# Create your views here.
from .models import Link


def links(request):
    links = Link.objects.filter(status=Link.STATUS_NORMAL)
    context = {
        'links':links
    }
    return render(request, template_name='config/links.html' , context=context)