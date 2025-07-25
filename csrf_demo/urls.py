import csrf_demo.views as csrf_demo
from django.urls import path

app_name = 'csrf_demo'
urlpatterns = [
    path("login/", csrf_demo.login, name='login')
]
