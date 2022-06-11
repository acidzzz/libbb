from django import forms

from .models import Book, ImageBook


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class ImageBookForm(forms.ModelForm):
    class Meta:
        model = ImageBook
        fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField()
