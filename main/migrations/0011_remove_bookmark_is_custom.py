# Generated by Django 4.2.5 on 2023-09-13 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_bookmark_name_alter_book_last_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='is_custom',
        ),
    ]
