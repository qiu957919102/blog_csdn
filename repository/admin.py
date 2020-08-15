from django.contrib import admin
from repository import models
# Register your models here.
"""
models.py 中定义了model，现在我们要在 admin 中对他们进行注册
注册模型使用 admin.site.register(model)方法进行注册：
"""
admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.UserFans)
admin.site.register(models.Category)
admin.site.register(models.ArticleDetail)
admin.site.register(models.UpDown)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
admin.site.register(models.Article)
admin.site.register(models.Article2Tag)
admin.site.register(models.Tpl)
admin.site.register(models.Trouble)