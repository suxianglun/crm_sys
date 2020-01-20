from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    # 昵称
    nick_name = models.CharField(verbose_name='昵称', max_length=60, blank=True)
    # 性别
    name = models.CharField(max_length=20, blank=True)
    # 性别
    sex = models.CharField(max_length=20, blank=True)
    # 电话
    tel = models.CharField(max_length=20, blank=True)
    # 公司
    company = models.CharField(max_length=60, blank=True)
    # 部门
    department = models.CharField(max_length=30, blank=True)
    # 岗位
    post = models.CharField(max_length=30, blank=True)
    # 微信号
    wechat = models.CharField(max_length=20, blank=True)
    # 创建时间
    create_time = models.DateTimeField(default=datetime.now)
    # 邮箱
    email = models.EmailField(blank=True)

    class Meta:
        # admin中显示的表名称
        verbose_name = '员工'
        # 不显示s
        verbose_name_plural = '员工'
