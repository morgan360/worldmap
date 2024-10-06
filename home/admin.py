from django.contrib import admin
from home.models import Feedback, ContactSubmission


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'comment']


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['submitted_at', 'email', 'message']
