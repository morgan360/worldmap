from django.urls import path
from api.views import  WorldDataView, serve_world_data_file
urlpatterns = [
    path('worlddata/', WorldDataView.as_view(), name='worlddata'),
    path('worlddata/<str:world_key>/', serve_world_data_file, name='serve_world_data_file'),
]

