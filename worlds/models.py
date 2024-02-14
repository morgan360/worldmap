from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supertype = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    creation_time_stamp = models.IntegerField(null=True, blank=True)
    image_url = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supertype = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    creation_time_stamp = models.IntegerField()  # Consider changing to DateTimeField
    image_url = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    physicality = models.TextField(blank=True, null=True)
    # species = models.ForeignKey('Species', on_delete=models.CASCADE, blank=True, null=True)
    traits = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    motivations = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    coercion = models.IntegerField(blank=True, null=True)
    capability = models.IntegerField(blank=True, null=True)
    compassion = models.IntegerField(blank=True, null=True)
    creativity = models.IntegerField(blank=True, null=True)
    courage = models.IntegerField(blank=True, null=True)
    corruption = models.TextField(blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    institutions = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    friends = models.TextField(blank=True, null=True)
    rivals = models.TextField(blank=True, null=True)
    relations = models.TextField(blank=True, null=True)
    hit_points = models.IntegerField(blank=True, null=True)
    # class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # 'class' is a reserved word in Python, hence the use of db_column to specify the actual database field.
    alignment = models.TextField(blank=True, null=True)
    inspirations = models.TextField(blank=True, null=True)
    tt_str = models.IntegerField(blank=True, null=True)
    tt_int = models.IntegerField(blank=True, null=True)
    tt_con = models.IntegerField(blank=True, null=True)
    tt_dex = models.IntegerField(blank=True, null=True)
    tt_wis = models.IntegerField(blank=True, null=True)
    tt_cha = models.IntegerField(blank=True, null=True)
    skill_stealth = models.IntegerField(blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    backpack = models.TextField(blank=True, null=True)
    proficiencies = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    spells = models.TextField(blank=True, null=True)
    birthplace = models.ForeignKey('Location', related_name='+', on_delete=models.SET_NULL, blank=True, null=True)
    # objects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

