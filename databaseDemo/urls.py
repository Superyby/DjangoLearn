from databaseDemo.views import index
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'databaseDemo'
urlpatterns = [
    path('', index, name='index'),  # 根路径
    path('data_index/', index, name='data_index'),  # 添加斜杠
]

# 添加静态文件支持
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)