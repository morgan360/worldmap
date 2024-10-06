from django.urls import path,include

from . import views
from .views import home, feedback_view, about, submit_contact_form, thanks_view, privacy_policy

urlpatterns = [
    path('', home, name='home'),
    path('logged-in-home/', home, name='logged_in_home'),
    path('feedback/', feedback_view, name='feedback'),
    path('about/', about, name='about'),
    path('contact/', submit_contact_form, name='submit_contact_form'),
    path('contact/thanks/', thanks_view, name='contact_thanks'),
    path('privacypolicy/', privacy_policy, name='privacy_policy'),
    path('webgl/', views.webgl, name='sikelia_webgl'),
    path('explorer/', views.explorer, name='explorer'),
]