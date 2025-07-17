from django.urls import path
import home.views as home_view

app_name = 'home'
urlpatterns = [
    path('index', home_view.index, name='index'),
    path('baidu', home_view.baidu, name='baidu'),
    path('info', home_view.info, name='info'),
    path('if', home_view.if_view, name='if'),
    path('for', home_view.for_view, name='for'),
    path('with', home_view.with_view, name='with'),
    path('url', home_view.url_view, name='url'),
]
