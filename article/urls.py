from django.urls import path
import article.views as article_view

app_name = 'article'
urlpatterns = [
    path('article_test/', article_view.article_test, name='article_test'),
    path('one_to_many/', article_view.one_to_many, name='one_to_many'),
    path('query1/', article_view.query1, name='query1'),
    path('query2/', article_view.query2, name='query2'),
    path('query3/', article_view.query3, name='query3'),
    path('query4/', article_view.query4, name='query4'),
    path('query5/', article_view.query5, name='query5'),
]
