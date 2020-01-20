from django.db import models

from user.models import User


class Company(models.Model):
    """
    公司
    """
    title = models.CharField(max_length=60)


class CustomerIndustry(models.Model):
    """
    客户行业
    """
    title = models.CharField(max_length=20)


class ClueSource(models.Model):
    """
    线索来源
    """
    title = models.CharField(max_length=20)


# Create your models here.
class Clue(models.Model):
    """
    线索
    """
    # 线索名称
    title = models.CharField(max_length=120)
    # 手机
    phone = models.CharField(max_length=20, blank=True)
    # 线索来源
    clue_source = models.OneToOneField(ClueSource, on_delete=models.CASCADE)
    # 电话
    tel = models.CharField(max_length=20, blank=True)
    # 客户行业
    customer_industry = models.OneToOneField(CustomerIndustry, on_delete=models.CASCADE)
    # 客户级别
    customer_level = models.CharField(max_length=20, blank=True)
    # 地址
    address = models.CharField(max_length=60, blank=True)
    # 下次联系时间
    next_time = models.DateField()
    # 创建人
    creator = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    """
    客户
    """
    # 客户名称
    name = models.CharField(max_length=120)
    # 客户等级
    level = models.IntegerField(choices=(('1', '普通客户'), ('2', '重点客户'), ('3', '其他客户')))
    # 客户行业
    customer_industry = models.OneToOneField(CustomerIndustry, on_delete=models.CASCADE)
    # 手机
    phone = models.CharField(max_length=20, blank=True)
    # 电话
    tel = models.CharField(max_length=20, blank=True)
    # 微信
    weChat = models.CharField(max_length=20, blank=True)
    # 网址
    website = models.CharField(max_length=120, blank=True)
    # 下次联系时间
    next_time = models.TimeField()
    # 备注
    next_time = models.TextField
    # 地址（省市区）
    address = models.CharField(max_length=120)
    # 详细地址
    detail_address = models.CharField(max_length=120)
    # 公司负责人
    head = models.OneToOneField(User, on_delete=models.CASCADE, related_name='head')
    # 创建人
    create_user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='create_user')
    # 是否进入公海
    is_open_sea = models.BooleanField()
    # 客户联系人


class Contact(models.Model):
    """
    联系人
    """
    name = models.CharField(max_length=20)
    # 所属客户
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # 手机
    phone = models.CharField(max_length=20, blank=True)
    # 电话
    tel = models.CharField(max_length=20, blank=True)
    # 微信
    weChat = models.CharField(max_length=20, blank=True)
    # 邮箱
    email = models.EmailField()
    # 是否是关键决策人
    is_key = models.BooleanField()
    # 职务
    job = models.CharField(max_length=20)
    # 性别
    sex = models.IntegerField(choices=(('1', '男'), ('2', '女')))
    # 下次联系时间
    next_time = models.TimeField()
    # 备注
    remark = models.TextField()


