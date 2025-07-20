from django.urls import path
import book.views as book_view

app_name = 'book'
urlpatterns = [
    path('add_book/', book_view.add_book, name='add_book'),
    path('query_book/', book_view.query_book, name='query_book'),
    path('order_view/', book_view.order_view, name='order_view'),
    path('update_view/', book_view.update_view, name='update_view'),
    path('delete_view/', book_view.delete_view, name='delete_view'),
    path('tag_view/', book_view.book_tag, name='tag_view')
]
