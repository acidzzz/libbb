# Generated by Django 4.0.5 on 2022-07-08 11:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('foto_author', models.ImageField(upload_to='images', verbose_name='Фотография автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_book_rus', models.CharField(max_length=100, verbose_name='Название книги')),
                ('name_book_origin', models.CharField(blank=True, max_length=100, null=True, verbose_name='Оригинальное название')),
                ('price_book', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('count_book', models.IntegerField(verbose_name='Количество')),
                ('price_one_day_period', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость одного дня')),
                ('year_published', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(0)], verbose_name='Год выпуска')),
                ('date_register_book_in_database', models.DateField(auto_now_add=True, verbose_name='Дата регистрации книги')),
                ('count_page_book', models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')),
                ('all_author_book', models.ManyToManyField(to='main.author', verbose_name='Все авторы книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_genre', models.CharField(max_length=30, unique=True, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='PersonReader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('patronymic', models.CharField(max_length=50, null=True, verbose_name='Отчество')),
                ('number_passport', models.CharField(max_length=9, unique=True, verbose_name='номер паспорта')),
                ('date_birthday', models.DateField(verbose_name='дата рождения')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('residential_address', models.CharField(max_length=100, null=True, verbose_name='Адрес проживания')),
                ('person_get_book', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
            ],
        ),
        migrations.CreateModel(
            name='ImageBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_book', models.ImageField(upload_to='images', verbose_name='Фотография обложки книги')),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book', verbose_name='книги')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_read_person',
            field=models.ManyToManyField(to='main.personreader', verbose_name='Читатели'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre_book',
            field=models.ManyToManyField(to='main.genre', verbose_name='Жанры книг'),
        ),
    ]
