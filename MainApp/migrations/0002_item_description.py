# Generated by Django 4.1.5 on 2023-02-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Базовое описание', max_length=1000),
        ),
    ]
