from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    name = models.CharField(max_length=50, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    @classmethod
    def get_navs(cls):
        categroys = cls.objects.filter(status=cls.STATUS_NORMAL)
        nav_categories = []
        normal_categories = []
        for categroy in categroys:
            if categroy.is_nav:
                nav_categories.append(categroy)
            else:
                normal_categories.append(categroy)

        return {
            'navs': nav_categories,
            'categories': normal_categories,
        }



    class Meta:
        verbose_name = verbose_name_plural = '分类'


class Tag(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )

    name = models.CharField(max_length=24, verbose_name='名称')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '标签'


class Post(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_DRAFT = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
        (STATUS_DRAFT, '草稿'),
    )

    title = models.CharField(max_length=255, verbose_name='标题')
    description = models.CharField(max_length=1024, blank=True,
                                   verbose_name='摘要')
    content = models.TextField(verbose_name='正文', help_text='正文必须是MarkDown格式')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,
                                         choices=STATUS_ITEMS,
                                         verbose_name='状态')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @staticmethod
    def get_by_tag(tag_id):
        try:
            tag = Tag.objects.get(tag_id)
        except Tag.DoesNotExist:
            tag = None
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')

        return post_list, tag


    @staticmethod
    def get_by_category(categroy_id):
        try:
            categroy = Category.objects.get(id=categroy_id)
        except Category.DoesNotExist:
            categroy = None
            post_list = []
        else:
            post_list = categroy.post_set.filter(status=Post.STATUS_NORMAL)\
                .select_related('owner', 'category')

        return post_list, categroy


    @classmethod
    def latest_posts(cls):
        queryset = cls.objects.filter(status=cls.STATUS_NORMAL)
        return queryset

    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']  # 根据id进行降序排列
