from django.shortcuts import render, HttpResponse
from book.models import *


# Create your views here.

def book_detail_query_string(request):
    book_id = request.GET.get("id")
    name = request.GET.get("name")
    return HttpResponse(f"book_id:{book_id},名称是:{name}")


def book_detail_path(request, book_id):
    return HttpResponse(f"book_id:{book_id}")


def book_str(request, book_id):
    return HttpResponse(f"str_book_id:{book_id}")


def book_slug(request, book_id):
    return HttpResponse(f"slug_book_id:{book_id}")


def book_path(request, book_id):
    return HttpResponse(f"path_book_id:{book_id}")


def add_book(request):
    book = Book(name='三国演义', author='罗贯中', price=50)
    book.save()
    return HttpResponse("图书添加成功")


def query_book(request):
    # books = Book.objects.all()
    books = Book.objects.filter(name="三国演义")
    # book = Book.objects.get(name="三国演义")
    for book in books:
        print(book.name, book.author, book.price)
    return HttpResponse("查询全部成功")


def order_view(request):
    # books = Book.objects.order_by("pub_time")
    books = Book.objects.all()
    for book in books:
        print(book.name, book.author, book.price)

    return HttpResponse("排序成功")


def update_view(request):
    book = Book.objects.first()
    book.name = "ok"
    book.save()
    return HttpResponse("修改ok")


def delete_view(request):
    book = Book.objects.filter(name="ok")
    book.delete()
    return HttpResponse("删除成功")


def book_tag(request):
    tag = Tag()
    tag.save()
    return HttpResponse("tag ok")
