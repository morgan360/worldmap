from django.db import models
from django.utils import timezone

#In Django, to share a set of fields across multiple models, you can use an abstract base class:
class BaseModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supertype = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
    creation_time_stamp = models.DateTimeField(default=timezone.now)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True



class Character(BaseModel):
    # Additional fields specific to Character
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


class Object(BaseModel):
    category = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value_per_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='objects')
    character = models.ForeignKey(Character, on_delete=models.SET_NULL, blank=True, null=True, related_name='objects')
    parent_object = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='child_objects')
    components = models.TextField(blank=True, null=True)
    rarity = models.CharField(max_length=255, blank=True, null=True)
    background = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Territory(BaseModel):
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='territories')
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True,
                                  related_name='territories')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='territories')
    size = models.IntegerField(blank=True, null=True)
    yield_field = models.IntegerField(blank=True, null=True,
                                      db_column='yield')  # 'yield' is a reserved keyword in Python, hence the use of db_column to specify the actual database field name.
    condition = models.TextField(blank=True, null=True)
    locations = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='owned_territories')

    def __str__(self):
        return self.name



class Location(BaseModel):
    institution_owner = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='owned_locations')
    character_owner = models.ForeignKey(Character, on_delete=models.SET_NULL, blank=True, null=True, related_name='owned_locations')
    coordinates = models.TextField(blank=True, null=True)
    parent_location = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='child_locations')
    maps = models.TextField(blank=True, null=True)
    pins = models.TextField(blank=True, null=True)
    founded_by = models.TextField(blank=True, null=True)
    primary_faction = models.TextField(blank=True, null=True)
    secondary_faction = models.TextField(blank=True, null=True)
    population_size = models.IntegerField(blank=True, null=True)
    faction_relations = models.TextField(blank=True, null=True)
    faction_assimilation = models.TextField(blank=True, null=True)
    hard_influence = models.TextField(blank=True, null=True)
    soft_influence = models.TextField(blank=True, null=True)
    rival = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='rival_locations')
    friend = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='friend_locations')
    local_government = models.TextField(blank=True, null=True)
    local_opposition = models.TextField(blank=True, null=True)
    regional_dominance = models.TextField(blank=True, null=True)
    regional_attitude = models.TextField(blank=True, null=True)
    territory = models.ForeignKey(Territory, on_delete=models.SET_NULL, blank=True, null=True, related_name='locations')
    primary_resource = models.TextField(blank=True, null=True)
    secondary_resources = models.TextField(blank=True, null=True)
    primary_industry = models.TextField(blank=True, null=True)
    secondary_industries = models.TextField(blank=True, null=True)
    generation_rate = models.TextField(blank=True, null=True)
    industry_rate = models.TextField(blank=True, null=True)
    build_emphasis = models.TextField(blank=True, null=True)
    build_rate = models.TextField(blank=True, null=True)
    primary_generation_offload = models.TextField(blank=True, null=True)
    primary_industry_offload = models.TextField(blank=True, null=True)
    secondary_generation_offloads = models.TextField(blank=True, null=True)
    secondary_industry_offloads = models.TextField(blank=True, null=True)
    coinage = models.TextField(blank=True, null=True)
    terrain_quality = models.TextField(blank=True, null=True)
    harbor_quality = models.TextField(blank=True, null=True)
    regional_role = models.TextField(blank=True, null=True)
    global_role = models.TextField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    operational_strengths = models.TextField(blank=True, null=True)
    natural_defenses = models.TextField(blank=True, null=True)
    fortifications = models.TextField(blank=True, null=True)
    primary_fight_type = models.TextField(blank=True, null=True)
    secondary_fight_type = models.TextField(blank=True, null=True)
    primary_cult = models.TextField(blank=True, null=True)
    secondary_cults = models.TextField(blank=True, null=True)
    religious_significance = models.TextField(blank=True, null=True)
    founding_date = models.IntegerField(blank=True, null=True)
    government_type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Institution(BaseModel):
    parent_institution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='child_institutions')
    primary_object = models.ForeignKey('Object', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='owned_institutions')
    god = models.ForeignKey('Force', on_delete=models.SET_NULL, blank=True, null=True)
    wealth = models.IntegerField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    cooperates = models.TextField(blank=True, null=True)
    members = models.TextField(blank=True, null=True)
    collectives = models.TextField(blank=True, null=True)
    philosophy = models.TextField(blank=True, null=True)
    child_institutions = models.TextField(blank=True,
                                          null=True)  # Assuming this field is meant to list IDs or names, consider redesigning this relationship if it should represent a ForeignKey or ManyToManyField.

    def __str__(self):
        return self.name

class Family(BaseModel):
    characters = models.TextField(blank=True,
                                  null=True)  # Consider using a ManyToManyField if this represents a relationship to the Character model
    size = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    founding_member = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='founded_families')
    members = models.TextField(blank=True,
                               null=True)  # As with 'characters', consider a ManyToManyField for actual relationships
    ambition = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Species(BaseModel):
    life_span = models.IntegerField(blank=True, null=True)
    average_weight = models.IntegerField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    habitats = models.TextField(blank=True, null=True)
    agency = models.TextField(blank=True, null=True)
    primary_trait = models.ForeignKey('Trait', on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='species')

    def __str__(self):
        return self.name


# Creature model
class Creature(BaseModel):
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    demeanour = models.TextField(blank=True, null=True)
    life_style = models.TextField(blank=True, null=True)
    territory = models.ForeignKey('Territory', on_delete=models.SET_NULL, blank=True, null=True, related_name='creatures')

    def __str__(self):
        return self.name

# Collective model
class Collective(BaseModel):
    amount = models.IntegerField(blank=True, null=True)
    primary_species = models.ForeignKey('Species', on_delete=models.SET_NULL, blank=True, null=True, related_name='collectives')
    characters = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    formation_date = models.IntegerField(blank=True, null=True)
    temperance = models.TextField(blank=True, null=True)
    parent_collective = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='child_collectives')
    parent_institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='collectives')

    def __str__(self):
        return self.name

class Trait(BaseModel):
    charisma = models.IntegerField(blank=True, null=True)
    coercion = models.IntegerField(blank=True, null=True)
    capability = models.IntegerField(blank=True, null=True)
    chastity = models.IntegerField(blank=True, null=True)
    creativity = models.IntegerField(blank=True, null=True)
    courage = models.IntegerField(blank=True, null=True)
    compassion = models.IntegerField(blank=True, null=True)
    physical_effects = models.TextField(blank=True, null=True)
    mental_effects = models.TextField(blank=True, null=True)
    behaviour_effects = models.TextField(blank=True, null=True)
    ability_effects = models.TextField(blank=True, null=True)
    character_carriers = models.TextField(blank=True, null=True)
    creature_carriers = models.TextField(blank=True, null=True)
    antithesis_trait = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='antithesis_of')

    def __str__(self):
        return self.name

class Force(BaseModel):
    frequency = models.IntegerField(blank=True, null=True)
    origins = models.TextField(blank=True, null=True)
    catalyst = models.ForeignKey(Object, on_delete=models.SET_NULL, blank=True, null=True, related_name='forces')
    manifesters = models.TextField(blank=True, null=True)
    effects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name




class Title(BaseModel):
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    collective = models.ForeignKey('Collective', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    territory = models.ForeignKey('Territory', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    secondary_character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True, related_name='secondary_titles')
    creature = models.ForeignKey('Creature', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    value = models.IntegerField(blank=True, null=True)
    max_value = models.IntegerField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ability(BaseModel):
    is_magic = models.BooleanField(default=False)
    cooldown = models.IntegerField(blank=True, null=True)
    effects = models.TextField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    linked_trait = models.ForeignKey('Trait', on_delete=models.SET_NULL, blank=True, null=True, related_name='abilities')
    character_carriers = models.TextField(blank=True, null=True)
    difficulty = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Language(BaseModel):
    origin_date = models.IntegerField(blank=True, null=True)
    prose = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Law(BaseModel):
    writing_date = models.IntegerField(blank=True, null=True)
    prohibitions = models.TextField(blank=True, null=True)
    passed_by = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='laws')
    territories = models.TextField(blank=True, null=True)
    maximum_fine = models.TextField(blank=True, null=True)
    intent = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Relation(BaseModel):
    primary_character = models.ForeignKey(
        'Character', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='primary_relations'
    )
    primary_institution = models.ForeignKey(
        'Institution', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='primary_relations'
    )
    secondary_character = models.ForeignKey(
        'Character', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='secondary_relations'
    )
    secondary_institution = models.ForeignKey(
        'Institution', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='secondary_relations'
    )
    debt = models.IntegerField(blank=True, null=True)
    secondary_debt = models.IntegerField(blank=True, null=True)
    debt_currency = models.TextField(blank=True, null=True)
    debt_type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Event(BaseModel):
    date = models.IntegerField(blank=True, null=True)
    proceedings = models.TextField(blank=True, null=True)
    affected_element = models.TextField(blank=True, null=True)
    affected_elements = models.TextField(blank=True, null=True)
    intensity = models.IntegerField(blank=True, null=True)
    adversity = models.TextField(blank=True, null=True)
    timestate = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Construct(BaseModel):
    origin = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
