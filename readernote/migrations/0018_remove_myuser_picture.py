# Generated by Django 3.0.8 on 2020-10-05 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0017_auto_20200928_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='picture',
        ),
    ]
