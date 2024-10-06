from django.urls import path
from .views import my_signup_view, update_profile, view_profile, my_login_view

urlpatterns = [
    path('accounts/signup/', my_signup_view, name='signup'),
    path('accounts/login/', my_login_view, name ='login'),
    path('profile/update/', update_profile, name='update_profile'),
    path('profile/', view_profile, name='view_profile'),
]