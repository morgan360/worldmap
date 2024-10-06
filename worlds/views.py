from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from tablib import Dataset
import json
import logging
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from api.models import WorldData
from django.http import HttpResponseRedirect
from django.urls import reverse


# Set up logging
logger = logging.getLogger(__name__)


@require_http_methods(["GET", "POST"])
def upload_json(request):
    if request.method == "POST":
        json_file = request.FILES.get('json_file')
        if json_file:
            try:
                json_data = json.load(json_file)

                # Extract character data from the nested structure
                characters_data = json_data.get("Character", [])
                if characters_data:
                    dataset = Dataset()
                    dataset.headers = characters_data[0].keys()
                    for character in characters_data:
                        dataset.append([character.get(field) for field in dataset.headers])

                    character_resource = CharacterResource()
                    result = character_resource.import_data(dataset, dry_run=False)  # Change to False to apply changes

                    if result.has_errors():
                        for errors in result.row_errors():
                            row_index, error_objects = errors[0], errors[1]
                            for error_object in error_objects:
                                # Retrieve the actual error message from each Error object
                                error_message = f"Row {row_index + 1}: {error_object.error}"
                                messages.error(request, error_message)
                                logger.error(error_message)
                    else:
                        messages.success(request, "Import completed successfully.")
                        if dry_run:
                            # Reminder to turn off dry_run for actual import
                            messages.info(request, "This was a dry run. No data was actually imported.")
                else:
                    messages.error(request, "No character data found in the uploaded file.")
            except json.JSONDecodeError as e:
                messages.error(request, "Invalid JSON file.")
                logger.error(f"JSON decode error: {str(e)}")
            except Exception as e:
                messages.error(request, "An unexpected error occurred during import.")
                logger.error(f"Unexpected error: {str(e)}")
        else:
            messages.error(request, "No file was uploaded.")
        return redirect('upload_json')
    return render(request, 'upload_json.html')



@login_required
def world_key_input(request):
    return render(request, 'world_key_input.html')


def world_key_input_process(request):
    # Get 'worldKey' from the query parameters
    world_key = request.GET.get('worldKey')

    if world_key:
        # Check if the worldKey exists in the database
        if WorldData.objects.filter(worldKey=world_key).exists():
            # Redirect to the detailed view with the world_key
            detail_url = reverse('world_data_detail', kwargs={'world_key': world_key})
            return HttpResponseRedirect(detail_url)
        else:
            # If worldKey does not exist, redirect back with an error message
            messages.error(request, 'The provided world key does not exist.')
            return redirect('world_key_input')
    else:
        # If worldKey is not provided, redirect back to the input form
        messages.error(request, 'No world key provided.')
        return redirect('world_key_input')



@login_required
def world_data_detail(request, world_key):
    try:
        world_data_instance = WorldData.objects.get(worldKey=world_key)
        # Assuming your model's file field is named `dataFile`
        if world_data_instance.dataFile:
            with open(world_data_instance.dataFile.path, 'r') as file:
                world_data = json.load(file)
        else:
            world_data = {}
    except WorldData.DoesNotExist:
        world_data = {}

    return render(request, 'world_data_detail.html', {'world_data': world_data})