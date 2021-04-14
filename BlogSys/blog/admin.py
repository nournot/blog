from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin

# Register your models here

from .adminforms import PostAdminForm
from .models import Category, Tag, Post

# 在分类的编辑页，下方新增一个编辑文章的组件
from BlogSys.custom_site import custom_site


class PostInline(admin.TabularInline):  # StackedInline样式不同
    fields = ('title', 'description')
    extra = 1  # 控制额外多几个
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline, ]

    list_display = ['name', 'is_nav', 'status', 'created_time', 'owner',
                    'post_count']
    fields = ['name', 'status', 'is_nav', ]

    # 展示中的自定义字段
    def post_count(self, obj):
        return obj.post_set.count()

    # 重写save_model，由django调用
    # 其中参数obj为要保存的对象。form为提交过来的表单。change用于标记本次保存是新增还是更新
    # 这里的obj是blog.models.Category对象
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'owner', 'created_time']
    fields = ['name', 'status', ]

    # 保存时，自动获取登陆用户，设置为创建者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id',
                                                                       'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(admin.ModelAdmin):
    # 自定义amdin的form
    form = PostAdminForm

    # 列表页面
    list_display = ['title', 'category', 'description', 'status',
                    'owner', 'created_time', 'operater']
    list_display_links = None

    # 列表页面，搜索栏、右侧过滤器
    # list_filter = ['category', ]
    list_filter = [CategoryOwnerFilter, ]
    search_fields = ['title', 'category__name']

    # 列表页面，处理行为栏，默认有批量删除
    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    # exclude = ('owner',)
    save_on_top = True

    # fields = [
    #     ('title', 'category'),
    #     'description',
    #     'status',
    #     'tags',
    #     'content',
    # ]

    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'description',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('collapse',),
            'fields': ('tags',),
        })
    )

    filter_horizontal = ('tags',)

    # filter_vertical = ('tags', )

    # 这是一个自定义方法，由django调用，obj也由他传入
    # 用于list_display中，作为展示自定义字段
    def operater(self, obj):
        return format_html(
            '<a href ="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operater.short_description = '操作'

    # 保存时，自动获取登陆用户，设置为创建者
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    # 重新，使只展示自己的文章列表
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user',
                    'change_message']
