from django.urls import path
import movie.views as movie_view

# 指定命名空间
app_name = 'movie'

urlpatterns = [
    path('list', movie_view.movie_list, name='movie_list'),
    path('detail/<int:movie_id>', movie_view.movie_detail, name='movie_detail'),
]
