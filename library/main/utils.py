# from models import Book, PersonReader
#
# import datetime
# def func(date_get, date_return, ):
#     date_get = PersonReader.person_get_book
#     date_return =
# b = PersonReader.person_get_book()
# a = a.split('-')
# b = b.split('-')
# aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
# bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
# cc = aa - bb
# print(cc)  # output days and time
from .models import Book


def discont(book_set):
    full_price=0
    if len(book_set)==1:
        for f in book_set:
            full_price+= Book.objects.get(name_book_rus=f).price_one_day_period*30
    elif len(book_set)==2 or len(book_set)==3 :
        for f in book_set:
            full_price += Book.objects.get(name_book_rus=f).price_one_day_period * 30*0.9
    elif len(book_set)==4:
        for f in book_set:
            full_price += Book.objects.get(name_book_rus=f).price_one_day_period * 30 * 0.85
    return full_price