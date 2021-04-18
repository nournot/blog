from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Post, Category


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'categroy':category,
        'tag':tag,
        'post_list':post_list,
    }
    context.update(Category.get_navs())

    return render(request, 'blog/list.html', context=context)

    # post_list = Post.objects.all()
    # context = {
    #     'post_list':post_list,
    # }
    # return render(request,'blog/list.html', context=context)

    # content = f'post_list category_id={category_id}, tag_id={tag_id}'.format(
    #     category_id=category_id, tag_id=tag_id)
    # return HttpResponse(content)


def detail(request, post_id=None):
    post = get_object_or_404(Post, pk=post_id)
    context ={
        'post':post,
    }
    return render(request, 'blog/detail.html', context=context)

    # return HttpResponse('detail')