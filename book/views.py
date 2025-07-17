from django.shortcuts import render, HttpResponse


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
