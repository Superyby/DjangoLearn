from django.shortcuts import render, HttpResponse


# Create your views here.

def movie_list(request):
    return HttpResponse("movie_list")


def movie_detail(request, movie_id):
    return HttpResponse(f"movie_id:{movie_id}")
