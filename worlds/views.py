from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from tablib import Dataset
from .resources import CharacterResource
import json
import logging
from django.shortcuts import render, redirect
from .forms import LocationForm
from django.http import HttpResponse
from .models import Location

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


def list_locations(request):
    locations = Location.objects.all()  # Query all locations
    return render(request, 'list_locations.html', {'locations': locations})


def create_location(request):
    if request.method == 'POST':
        print('Posted')
        form = LocationForm(request.POST)
        if form.is_valid():
            print('Valid')
            form.save()
            return redirect('list_locations')  # Redirect to a success URL
    else:
        form = LocationForm()

    return render(request, 'create_location.html', {'form': form})

def edit_location(request, id):
    # Assuming 'Location' is your model and 'LocationForm' is your form
    location = get_object_or_404(Location, id=id)
    if request.method == 'POST':
        form = LocationForm(request.POST, instance=location)
        if form.is_valid():
            form.save()
            # Redirect to a success page, for example, the list locations page
            return redirect('list_locations')
    else:
        form = LocationForm(instance=location)
    return render(request, 'edit_location.html', {'form': form})