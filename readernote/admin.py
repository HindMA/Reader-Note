from django.contrib import admin

# Register your models here.
from .models import MyUser,user_info_for_download_free, addUpdate, myfavourite, article, book, broadcast, lecture, video, article_comments, article_dates, article_freespaces, article_ideas, article_questions, article_subjects, article_terms, article_trans, book_comments, book_dates, book_freespaces, book_ideas, book_questions, book_subjects, book_terms, book_trans, broadcast_comments, broadcast_dates, broadcast_freespaces, broadcast_ideas, broadcast_questions, broadcast_subjects, broadcast_terms, broadcast_trans, lecture_comments, lecture_dates, lecture_freespaces, lecture_ideas, lecture_questions, lecture_subjects, lecture_terms, lecture_trans, video_comments, video_dates, video_freespaces, video_ideas, video_questions, video_subjects, video_terms, video_trans, post

admin.site.register(MyUser)
admin.site.register(user_info_for_download_free)
admin.site.register(myfavourite)
admin.site.register(addUpdate)

admin.site.register(article)
admin.site.register(article_comments)
admin.site.register(article_dates)
admin.site.register(article_freespaces)
admin.site.register(article_ideas)
admin.site.register(article_questions)
admin.site.register(article_subjects)
admin.site.register(article_terms)
admin.site.register(article_trans)

admin.site.register(book)
admin.site.register(book_comments)
admin.site.register(book_ideas)
admin.site.register(book_questions)
admin.site.register(book_terms)
admin.site.register(book_subjects)
admin.site.register(book_dates)
admin.site.register(book_trans)
admin.site.register(book_freespaces)

admin.site.register(broadcast)
admin.site.register(broadcast_comments)
admin.site.register(broadcast_ideas)
admin.site.register(broadcast_questions)
admin.site.register(broadcast_terms)
admin.site.register(broadcast_subjects)
admin.site.register(broadcast_dates)
admin.site.register(broadcast_trans)
admin.site.register(broadcast_freespaces)

admin.site.register(lecture)
admin.site.register(lecture_comments)
admin.site.register(lecture_ideas)
admin.site.register(lecture_questions)
admin.site.register(lecture_terms)
admin.site.register(lecture_subjects)
admin.site.register(lecture_dates)
admin.site.register(lecture_trans)
admin.site.register(lecture_freespaces)

admin.site.register(video)
admin.site.register(video_comments)
admin.site.register(video_ideas)
admin.site.register(video_questions)
admin.site.register(video_terms)
admin.site.register(video_subjects)
admin.site.register(video_dates)
admin.site.register(video_trans)
admin.site.register(video_freespaces)

admin.site.register(post)
