from django.db import models
from django.core import validators


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100, validators=[validators.MinLengthValidator(limit_value=2)])
    content = models.TextField(validators=[validators.MinLengthValidator(limit_value=3)])
    # 指定了auto_now_add=True 在表单里可以不用传这个参数
    create_time = models.DateTimeField(auto_now_add=True)
    # blank=True 只是表单验证时允许为空 不代表数据库为空
    category = models.CharField(max_length=100, blank=False)
