from django.shortcuts import render, redirect
from .models import Coordinates
from .forms import CoordinatesForm, DeleteCoordinatesForm
import folium

def coordinates_form(request):
    coordinates = Coordinates.objects.all()
    form = CoordinatesForm()

    if request.method == 'POST':
        form = CoordinatesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("maps")  # Corrected indentation and placement

    context = {
        'coordinates': coordinates,
        'form': form,
    }
    return render(request, 'maps/maps_form.html', context)

def maps(request):
    coordinates_list = Coordinates.objects.values_list('latitude', 'longitude')

    map = folium.Map(location=[0, 0], zoom_start=2)

    for latitude, longitude in coordinates_list:  # Corrected spelling
        folium.Marker([latitude, longitude]).add_to(map)

    folium.raster_layers.TileLayer('Stamen Terrain').add_to(map)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(map)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(map)
    folium.LayerControl().add_to(map)

    map = map._repr_html_()
    context = {
        'map': map,
    }
    return render(request, 'maps/maps.html', context)


def delete_coordinates(request):
    if request.method == 'POST':
        delete_form = DeleteCoordinatesForm(request.POST)
        if delete_form.is_valid():
            coordinates_to_delete = delete_form.cleaned_data['coordinates_to_delete']
            coordinates_to_delete.delete()
            return redirect("maps")

    delete_form = DeleteCoordinatesForm()
    context = {
        'delete_form': delete_form,
    }
    return render(request, 'maps/delete_form.html', context)

