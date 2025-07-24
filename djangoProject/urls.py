"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import HttpResponse

import home
from book import views as book_view
from django.urls import reverse


# from movie import views as movie_view
# from home import views as home_view


# www.baidu.com/y?wd=python
# URL与视图的映射
# /y(URL) -> 视图函数，进行映射

def index(request):
    # print(reverse('book_detail_query_string'))
    # /book/str/1
    print(reverse("book_str", kwargs={"book_id": 1}))

    # /book/id?1
    print(reverse("book_detail_query_string") + "?book_id=1")

    # 带命名空间
    print(reverse("movie:movie_list"))

    # 上面的3个输出在 ''的index路径里只会输出hello
    return HttpResponse("hello")


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name="index"),
    # include()   movie/加了斜杠在视图函数就不用了
    path("movie/", include("movie.urls")),
    path("home/", include("home.urls")),
    path("data/", include("databaseDemo.urls")),
    path("book/", include("book.urls")),
    path("article/", include("article.urls")),
    path("front/", include("front.urls")),
    path("form_demo/", include("form_demo.urls")),
]
