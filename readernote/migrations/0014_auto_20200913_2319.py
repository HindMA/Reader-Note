# Generated by Django 3.0.8 on 2020-09-13 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0013_myuser_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='picture',
            field=models.FileField(upload_to=''),
        ),
    ]
