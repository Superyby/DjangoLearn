from django.shortcuts import render, HttpResponse


# Create your views here.

def add_cookie(request):
    response = HttpResponse('设置cookie')
    max_age = 60 * 60 * 24 * 7
    response.set_cookie("username", "yuuok", max_age=max_age)
    return response


def delete_cookie(request):
    response = HttpResponse('删除cookie')
    response.delete_cookie("username")
    return response


def get_cookie(request):
    # username = request.COOKIES.get("username")
    # print(username)
    # 也可以循环遍历
    for key, value in request.COOKIES.items():
        print(key, value)
    return HttpResponse("get cookie")


def add_session(request):
    request.session['user_id'] = 'yuuok'
    request.session.set_expiry(0)
    return HttpResponse('add_session')


def get_session(request):
    userid = request.session.get('user_id')
    print(userid)
    return HttpResponse(userid)
