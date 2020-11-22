# Generated by Django 3.0.8 on 2020-08-27 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readernote', '0006_book_terms_is_term'),
    ]

    operations = [
        migrations.AddField(
            model_name='article_comments',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_dates',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_freespaces',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_ideas',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_questions',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_subjects',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_terms',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='article_trans',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_comments',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_dates',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_freespaces',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_ideas',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_questions',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_subjects',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_terms',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='book_trans',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_comments',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_dates',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_freespaces',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_ideas',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_questions',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_subjects',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_terms',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='broadcast_trans',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_comments',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_dates',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_freespaces',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_ideas',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_questions',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_subjects',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_terms',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='lecture_trans',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_comments',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_dates',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_freespaces',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_ideas',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_questions',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_subjects',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_terms',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='video_trans',
            name='share',
            field=models.CharField(max_length=100, null=True),
        ),
    ]