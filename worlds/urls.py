from django.urls import path
from .views import upload_json, world_data_detail, world_key_input, \
    world_key_input_process

urlpatterns = [
    # Your other URLs...
    path('upload-json/', upload_json, name='upload_json'),
    path('worlddata/input/', world_key_input, name='world_key_input'),
    path('worlddata/process_input/', world_key_input_process, name='world_key_input_process'),
    path('worlddata/<str:world_key>/', world_data_detail, name='world_data_detail'),
]
