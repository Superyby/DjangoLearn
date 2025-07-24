from django.shortcuts import render, HttpResponse
from form_demo.forms import *
# 请求验证装饰器
from django.views.decorators.http import require_http_methods


# Create your views here.
# 请求的方法
#  GET：从服务器获取数据
#  POST：向服务器提交数据
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        form = MessageForm()
        return render(request, 'form_index.html', {'form': form})  # 把表单传过去
    elif request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            return HttpResponse(f'title:{title},content:{content},email:{email}')
        else:
            print(form.errors)
            return HttpResponse("表单验证失败")
