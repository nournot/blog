from django.contrib.admin import AdminSite

class CustomeSite(AdminSite):
    site_header = "Sven's Blog管理后台"
    site_title = "Blog"
    index_title = '首页'

custom_site = CustomeSite(name='cus_admin')
