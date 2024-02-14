from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Character, Location

class CharacterResource(resources.ModelResource):
    location = fields.Field(
        column_name='location',
        attribute='location',
        widget=ForeignKeyWidget(Location, 'id'))  # Assuming 'id' is what you want to match on

    class Meta:
        model = Character
        exclude = ('id',)  # Assuming you want to auto-generate new IDs
        import_id_fields = ['name']  # Use 'name' as a unique identifier for import