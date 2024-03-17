from django.urls import path
from api.views import ActorsListCreate, WorldDataView, serve_world_data_file
urlpatterns = [
    path('actors/', ActorsListCreate.as_view(), name='actors-list-create'),
    path('worlddata/', WorldDataView.as_view(), name='worlddata'),
    path('worlddata/<str:world_key>/', serve_world_data_file, name='serve_world_data_file'),
]

