import os
import random
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

def _upload_to(instance, filename):
    file_root, file_ext = os.path.splitext(filename)
    letters = [chr(i) for i in range(97, 123)]  # letters =['a','b','c','d',......'z']
    str_str = "".join(random.sample(letters, 3))
    str_num = repr(random.random()).replace(".", "")
    data = datetime.now().strftime("%Y/%j")
    random_filename = str_str + str_num + file_ext
    return "/".join([data, random_filename])


def showcase_upload_to(instance, filename):
    return "showcase/" + _upload_to(instance, filename)


def cover_upload_to(instance, filename):
    return "cover/" + _upload_to(instance, filename)


def slide_upload_to(instance, filename):
    return "slide/" + _upload_to(instance, filename)


def video_upload_to(instance, filename):
    return "videos/" + _upload_to(instance, filename)


class Tag(models.Model):
    # 标签用来对视频做标记,比如seo,上下架这样的标签,这样做的目的是为了检索方便
    # 一个视频可以有多个标签
    # 如果网站以后加入对博文的支持,那么一篇博文也可以有多个标签
    caption = models.CharField(max_length=50, unique=True, verbose_name="标签名称")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = "标签"


class TutorialCategory(models.Model):
    # 课程的分类,比如可能有文案系列,seo精讲,客服系列
    caption = models.CharField(max_length=20, verbose_name="名称")

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = '课程类别'
        verbose_name_plural = '课程类别'


class Tutorial(models.Model):
    caption = models.CharField(max_length=100, verbose_name="名称")
    cover = models.ImageField(verbose_name="封面", upload_to=cover_upload_to)
    showcase = models.ImageField(blank=True, verbose_name="横幅", upload_to=showcase_upload_to)
    intro = models.TextField(verbose_name="简介")
    intro1 = models.TextField(verbose_name="摘要")
    category = models.ForeignKey(TutorialCategory, verbose_name="课程类别")
    created = models.DateTimeField(auto_now_add=True, verbose_name="发表时间", blank=True)
    modified = models.DateTimeField(auto_now=True, verbose_name="修改时间", blank=True)
    length = models.CharField(max_length=20, verbose_name="总时长", blank=True)
    homepage = models.BooleanField(default=False, verbose_name="放到首页？")
    order_by = models.IntegerField(default=0, verbose_name='顺序')
    download_link = models.TextField(verbose_name='下载链接', default='#')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        ordering = ['order_by']


class Video(models.Model):
    # 一门课程有多个视频
    caption = models.CharField(max_length=200, verbose_name="标题")
    length = models.CharField(max_length=20, verbose_name="时长")
    tags = models.ManyToManyField(Tag, verbose_name="标签")
    tutorial = models.ForeignKey(Tutorial, verbose_name="课程")
    # file = models.FileField(verbose_name="视频文件", upload_to=video_upload_to)
    file = models.CharField(max_length=300, verbose_name='视频文件')
    order_by = models.IntegerField(default=0, verbose_name='顺序')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = '视频'
        ordering = ['order_by']


class Slide(models.Model):
    title = models.CharField(max_length=200, verbose_name='标题')
    description = models.CharField(max_length=200, verbose_name='描述')
    cover = models.ImageField(verbose_name="图片", upload_to=slide_upload_to)
    link = models.OneToOneField(Tutorial, verbose_name="链接到")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "走马灯"
        verbose_name_plural = "走马灯"


class Sms(models.Model):
    mobile = models.CharField(max_length=11)
    message = models.CharField(max_length=100)
    sendTime = models.DateTimeField()

    def __str__(self):
        return self.mobile + ',' + self.message

    class Meta:
        ordering = ['-sendTime']


class Commodity(models.Model):
    title = models.CharField(max_length=100, verbose_name="名称")
    description = models.TextField(verbose_name="描述")
    price = models.IntegerField(verbose_name="价格", blank=True)
    days = models.IntegerField(verbose_name="有效期(天数)")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"


class User_buy(models.Model):
    user = models.ForeignKey(User)
    commodity = models.ForeignKey(Commodity)
    start = models.DateField()
    expire = models.DateField()
    price = models.FloatField(default=0)
    order_id = models.CharField(max_length=64, default="#", blank=True)
    alipay_id = models.CharField(default="#", blank=True, max_length=100)
    payed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.user.username + '--' + self.commodity.title

    class Meta:
        ordering = ['-expire']


class Trade_bill(models.Model):
    bill_id = models.CharField(max_length=32, unique=True)
    alipay_id = models.CharField(max_length=100, blank=True)
    commodity = models.ForeignKey(Commodity)
    user = models.ForeignKey(User)
    start = models.DateField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.bill_id


class trace_code(models.Model):
    trace = models.CharField(max_length=100)
    when = models.DateTimeField()

    def __str__(self):
        return self.trace
