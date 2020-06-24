from django.shortcuts import render,HttpResponse
from myapp import models

# 测试git
def add_data(request):
    data = models.reg_mobile(meid="A10000000000000000",brand='荣耀',seller="京东",data_num="2008-8-8")
    data.save()
    return HttpResponse("<p>数据添加成功！</p>")