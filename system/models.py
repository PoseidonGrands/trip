from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField('名称', max_length=256)
    desc = models.CharField('描述', max_length=256, null=True)
    types = models.SmallIntegerField('轮播图属于哪个模块', default=10, null=True)
    img = models.ImageField('图片地址', max_length=256, upload_to='%Y%m/slider')
    target_url = models.CharField('目标地址', max_length=256)
    reorder = models.CharField('排序', max_length=256, null=True)
    is_valid = models.SmallIntegerField('是否有效', default=1)
    start_time = models.DateField('开始时间', null=True)
    end_time = models.DateField('结束时间', null=True)
    create_at = models.DateField('创建时间', auto_now_add=True)
    update_at = models.DateField('更新时间', auto_now=True)

    class Meta:
        db_table = 'system_slider'
        ordering = ['-reorder']


