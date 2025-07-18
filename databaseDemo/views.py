from django.shortcuts import render, HttpResponse
from django.db import connection


# Create your views here.
def index(request):
    # 获取游标对象
    cursor = connection.cursor()
    # 拿到对象后执行sql
    cursor.execute("select * from book")

    # 获取所有数据
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return HttpResponse("查询成功")
