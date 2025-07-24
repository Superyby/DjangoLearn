from django.shortcuts import render, HttpResponse
from article.models import *
from datetime import datetime


# Create your views here.
def article_test(request):
    # user = User(username="okkyu", password="123456")
    # user.save()
    # article = Article(title="测试文章", content="这是测试文章", author=user)
    # article.save()

    articles = Article.objects.first()
    return HttpResponse(articles.author.username)


# 获取某个用户的所有文章
def one_to_many(request):
    user = User.objects.first()
    # 设置了related_name就不用article_set了
    # article_list = user.article_set.all()
    article_list = user.articles.filter(title__contains='测试').all()
    for article in article_list:
        print(article.title)

    return HttpResponse("one_to_many")


def query1(request):
    # article = Article.objects.filter(id__exact='1')
    # article = Article.objects.filter(title__iexact='测试文章')
    article = Article.objects.filter(title__contains='测试')
    # 查询结果
    print(article.query)
    print(article)
    return HttpResponse("query1")


def query2(request):
    article = Article.objects.filter(title__contains='测试')
    print(article.query)
    print(article)
    return HttpResponse("query2")


def query3(request):
    article = Article.objects.filter(id__in=[1, 2, 3])
    print(article.query)
    print(article)
    return HttpResponse("query3")


def query4(request):
    start_date = datetime(2025, 7, 21)
    end_time = datetime(2025, 7, 23)
    article = Article.objects.filter(pub_time__range=(start_date, end_time))
    print(article)
    print(article.query)
    return HttpResponse("query4")


def query5(request):
    user = User.objects.filter(articles__title__icontains='测试')
    print(user.query)
    print(user)
    return HttpResponse("query5")
