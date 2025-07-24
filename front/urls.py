from django.urls import path
import front.views as front_view

app_name = 'front'
urlpatterns = [
    path('avg_view/', front_view.avg_view, name='avg_view'),
    path('count_view/', front_view.count_view, name='count_view'),
    path('max_min_view/', front_view.max_min_view, name='max_min_view'),
    path('sum_view/', front_view.sum_view, name='sum_view'),
    path('f_view/', front_view.f_view, name='f_view'),
    path('q_view/', front_view.q_view, name='q_view'),
]
