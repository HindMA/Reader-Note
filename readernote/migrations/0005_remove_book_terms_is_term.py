# Generated by Django 3.0.8 on 2020-08-27 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0004_auto_20200827_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_terms',
            name='is_term',
        ),
    ]
