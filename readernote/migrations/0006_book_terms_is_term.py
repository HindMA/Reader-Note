# Generated by Django 3.0.8 on 2020-08-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0005_remove_book_terms_is_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_terms',
            name='is_term',
            field=models.CharField(default='te', max_length=100),
            preserve_default=False,
        ),
    ]