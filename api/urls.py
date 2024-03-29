from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import  WorldDataView, serve_world_data_file, get_api_key


urlpatterns = [
    path('worlddata/', WorldDataView.as_view(), name='worlddata'),
    path('worlddata/<str:world_key>/', serve_world_data_file, name='serve_world_data_file'),
    path('get_api_key/', get_api_key, name='get_api_key'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

