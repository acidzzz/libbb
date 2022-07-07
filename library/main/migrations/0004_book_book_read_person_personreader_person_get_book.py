# Generated by Django 4.0.5 on 2022-07-07 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_book_genre_book_alter_genre_name_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_read_person',
            field=models.ManyToManyField(to='main.personreader', verbose_name='Читатели'),
        ),
        migrations.AddField(
            model_name='personreader',
            name='person_get_book',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выдачи'),
        ),
    ]