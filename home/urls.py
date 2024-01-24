from django.urls import path,include
from .views import home, feedback_view

urlpatterns = [
    path('', home, name='home'),
    path('logged-in-home/', home, name='logged_in_home'),
    path('feedback/', feedback_view, name='feedback'),
    ]