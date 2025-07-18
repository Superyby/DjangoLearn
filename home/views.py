from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, "index.html")


def baidu(request):
    return render(request, "baidu.html")


def info(request):
    # 普通变量
    username = "info"

    # 字典
    book = {
        "name": "水浒传",
        "author": "施耐庵"
    }
    # 列表
    books = [
        {'name': "水浒传", 'author': "施耐庵"},
        {'name': "三国演义", 'author': "罗贯中"}
    ]

    # 对象
    class Person:
        def __init__(self, realname):
            self.realname = realname

    context = {
        'username': username,
        'books': books,
        'book': book,
        'person': Person("yu")
    }
    return render(request, "info.html", context=context)


def if_view(request):
    age = 17
    context = {
        'age': age
    }
    return render(request, "if.html", context=context)


def for_view(request):
    # 列表
    books = [
        # {'name': "水浒传", 'author': "施耐庵"},
        # {'name': "三国演义", 'author': "罗贯中"}
    ]

    # 字典
    person = {
        "realname": "yu",
        "age": "17",
        "height": 170
    }

    context = {
        "books": books,
        "person": person
    }
    return render(request, "for.html", context=context)


def with_view(request):
    context = {
        "books": [
            {"name": "水浒传", "author": "施耐庵"},
            {"name": "三国演义", "author": "罗贯中"}
        ]
    }
    return render(request, "with.html", context=context)


def url_view(request):
    context = {
        "username": "yu"
    }
    return render(request, "url.html", context=context)


def book_detail(request, book_id):
    return HttpResponse(f"book_id: {book_id}")


def filter_view(request):
    greet = "hello world ,nihao django"
    context = {
        "greet": greet,
        "birthday": datetime.now(),
        "profile": "",
        "html": "<h1>hello world yu</h1>"
    }
    return render(request, "filter.html", context=context)


def template_form(request):
    context = {
        'articles': ['小米su7', 'chat gpt']
    }
    return render(request, "xfz_index.html", context=context)


def static_view(request):
    return render(request, "static.html")
