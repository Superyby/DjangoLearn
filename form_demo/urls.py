from django.urls import path
import form_demo.views as form_demo

app_name = 'form_demo'
urlpatterns = [
    path('index/', form_demo.index, name='form_index'),
    path('register/', form_demo.register_view, name='form_register'),
    path('article_view/', form_demo.article_view, name='article_view'),
]
