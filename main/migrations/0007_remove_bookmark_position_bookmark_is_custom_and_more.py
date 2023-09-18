# Generated by Django 4.2.5 on 2023-09-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_bookmark_page_book_epub_viewer_key_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmark',
            name='position',
        ),
        migrations.AddField(
            model_name='bookmark',
            name='is_custom',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
