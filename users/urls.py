from django.urls import path

from home.views import CustomLoginView
from .views import my_signup_view, update_profile, view_profile

urlpatterns = [
    path('accounts/signup/', my_signup_view, name='signup'),
    path('accounts/login/', CustomLoginView.as_view(), name='account_login'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/', view_profile, name='view_profile'),
]