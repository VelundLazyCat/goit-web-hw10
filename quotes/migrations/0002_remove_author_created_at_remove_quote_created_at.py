# Generated by Django 5.1.3 on 2024-12-03 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='created_at',
        ),
    ]