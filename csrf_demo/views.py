from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
# @csrf_exempt
@require_http_methods(['POST', 'GET'])
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        print(request.POST)  # 查看提交的数据
        print(request.COOKIES)
    return HttpResponse('登录成功')
