from django.db import models

# Create your models here.
class reg_mobile(models.Model):
    id = models.AutoField(primary_key=True) # id 会自动创建,可以手动写入
    meid = models.CharField(max_length=32) # 书籍名称
    imei1 = models.CharField(max_length=32) # 书籍价格
    brand = models.CharField(max_length=32)
    seller = models.CharField(max_length=32) # 出版社名称
    sell_num_day =models.CharField(max_length=32) # 出版时间
    sell_num_week = models.CharField(max_length=32)
    sell_num_month = models.CharField(max_length=32)
    sell_num_year = models.CharField(max_length=32)
    sell_num_all = models.CharField(max_length=32)
    data_num = models.DateField()