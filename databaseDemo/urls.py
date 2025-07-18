from django.urls import reverse
import databaseDemo.views as data_view
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


app_name = 'databaseDemo'
urlpatterns = [
    path('data_index', data_view.index, name='index'),
]