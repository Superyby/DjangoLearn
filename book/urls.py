from django.urls import path
import book.views as book_view

app_name = 'book'
urlpatterns = [
    # 127.0.0.1:8000/book/id=1&name=111
    path("book/", book_view.book_detail_query_string, name="book_detail_query_string"),
    # 127.0.0.1:8000/book/1
    path("book/<int:book_id>", book_view.book_detail_path, name="book_detail_path"),  # 默认是str类型
    path("book/str/<str:book_id>", book_view.book_str, name="book_str"),
    path("book/slug/<slug:book_id>", book_view.book_slug, name="book_slug"),
    path("book/path/<path:book_id>", book_view.book_path, name="book_path"),
    path('add_book/', book_view.add_book, name='add_book'),
    path('query_book/', book_view.query_book, name='query_book'),
    path('order_view/', book_view.order_view, name='order_view'),
    path('update_view/', book_view.update_view, name='update_view'),
    path('delete_view/', book_view.delete_view, name='delete_view'),
    path('tag_view/', book_view.book_tag, name='tag_view')
]
