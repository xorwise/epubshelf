# Generated by Django 4.2.5 on 2023-09-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_user_last_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='payment_active',
            field=models.BooleanField(default=True),
        ),
    ]