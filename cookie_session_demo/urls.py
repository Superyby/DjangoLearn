from django.urls import path
import cookie_session_demo.views as cookie_session_view

app_name = 'cookie_session_demo'
urlpatterns = [
    path('add_cookie/', cookie_session_view.add_cookie, name='add_cookie'),
    path('delete_cookie/', cookie_session_view.delete_cookie, name='delete_cookie'),
    path('get_cookie/', cookie_session_view.get_cookie, name='get_cookie'),
    path('add_session/', cookie_session_view.add_session, name='add_session'),
    path('get_session/', cookie_session_view.get_session, name='get_session'),
]
