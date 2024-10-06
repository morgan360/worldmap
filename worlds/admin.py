# # # @admin.register(Character)
# # # class CharacterAdmin(admin.ModelAdmin):
# # #     list_display = ('name', 'appearance', 'age', 'location')
# # #     search_fields = ('name', 'location')
# #
# # @admin.register(Object)
# # class ObjectAdmin(admin.ModelAdmin):
# #     list_display = ('name', 'aesthetics', 'weight', 'parent_object')
# #     search_fields = ('name', 'aesthetics')
#
# @admin.register(Creature)
# class CreatureAdmin(admin.ModelAdmin):
#     list_display = ('name', 'physicality', 'weight', 'location', 'species')
#     search_fields = ('name', 'species')

# from django.contrib import admin
# from .models import Location, Character, Object, Creature, Institution  # Adjust the import path as necessary

# Register your models here.

# @admin.register(Location)
# class LocationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'population', 'population_size', 'parent_location')
#     search_fields = ('name', 'population')

# @admin.register(Institution)
# class InstitutionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'basis', 'parent_institution')
#     search_fields = ('name', 'basis')

