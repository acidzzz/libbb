# Generated by Django 4.0.5 on 2022-07-13 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_read_person',
            field=models.ManyToManyField(blank=True, null=True, to='main.personreader', verbose_name='Читатели'),
        ),
    ]
