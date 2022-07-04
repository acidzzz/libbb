from django.urls import path


from .views import page_index, image_add, main_page, add_reader, add_author, book_genre_popup_add, \
    book_author_popup_add, readers_page, BookListView, GetDiscriptionBook

app_name = 'lib'

urlpatterns = [
    path('register_book/', page_index, name='page_index'),
    path('image_add/', image_add, name='image_add'),
    # path('', main_page, name='main_page'),
    path('add_reader/', add_reader, name='add_reader'),
    path('add_author/', add_author, name='add_author'),
    path('register_book1/', book_genre_popup_add, name='book_genre_popup_add'),
    path('register_book2/', book_author_popup_add, name='book_author_popup_add'),
    path('readers/', readers_page, name='readers_page'),
    path('', BookListView.as_view(), name='main_page'),
    path('book/<int:pk>', GetDiscriptionBook.as_view(), name='get_discription_book')
]
