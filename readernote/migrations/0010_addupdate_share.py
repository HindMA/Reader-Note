# Generated by Django 3.0.8 on 2020-09-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0009_auto_20200901_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='addupdate',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
