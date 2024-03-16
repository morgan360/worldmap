from django.db import models


class BaseModel(models.Model):
    id = models.TextField(blank=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


# Create your models here.
class Location(BaseModel):
    population = models.TextField(blank=True, null=True)
    population_size = models.IntegerField(blank=True, null=True)
    parent_location = models.TextField(blank=True, null=True)
    founded_by = models.TextField(blank=True, null=True)
    maps = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)


class Character(BaseModel):
    appearance = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Object(BaseModel):
    aesthetics = models.TextField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    parent_object = models.TextField(blank=True, null=True)
    technology = models.TextField(blank=True, null=True)
    components = models.TextField(blank=True, null=True)


class Creature(BaseModel):
    physicality = models.TextField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)


class Institution(BaseModel):
    basis = models.TextField(blank=True, null=True)
    parent_institution = models.TextField(blank=True, null=True)
    creatures = models.TextField(blank=True, null=True)
