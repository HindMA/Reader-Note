# Generated by Django 3.0.8 on 2020-09-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0012_auto_20200901_0801'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='picture',
            field=models.ImageField(default='none', upload_to=''),
            preserve_default=False,
        ),
    ]