from django.contrib import admin
from home.models import Feedback


@admin.register(Feedback)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['user', 'rating', 'comment']