from django.urls import path
import home.views as home_view
from django.conf.urls.static import static
from django.conf import settings

app_name = 'home'
urlpatterns = [
    path('index', home_view.index, name='index'),
    path('baidu', home_view.baidu, name='baidu'),
    path('info', home_view.info, name='info'),
    path('if', home_view.if_view, name='if'),
    path('for', home_view.for_view, name='for'),
    path('with', home_view.with_view, name='with'),
    path('url', home_view.url_view, name='url'),
    path('book/<int:book_id>', home_view.book_detail, name='book_detail'),
    path('filter', home_view.filter_view, name='filter'),
    path('template/form', home_view.template_form, name='template_form'),
    path('template/sta', home_view.static_view, name='sta')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
