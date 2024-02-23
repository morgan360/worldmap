from django.db import models
from django.utils import timezone

#In Django, to share a set of fields across multiple models, you can use an abstract base class:
class BaseModel(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supertype = models.CharField(max_length=255, blank=True, null=True)
    subtype = models.CharField(max_length=255, blank=True, null=True)
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
    species = models.ForeignKey('Species', on_delete=models.CASCADE, blank=True, null=True)
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
    class_field = models.CharField(db_column='class', max_length=255, blank=True, null=True)  # 'class' is a reserved word in Python, hence the use of db_column to specify the actual database field.
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
    objects = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Object(BaseModel):
    category = models.CharField(max_length=255, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    value_per_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='objects')
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True, related_name='objects')
    parent_object = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='child_objects')
    components = models.TextField(blank=True, null=True)
    rarity = models.TextField(blank=True, null=True)
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
                                      db_column='yield')
    condition = models.TextField(blank=True, null=True)
    locations = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    owner = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True,
                              related_name='owned_territories')

    def __str__(self):
        return self.name



class Character(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    physicality = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    motivations = models.TextField(blank=True, null=True)
    situation = models.TextField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    coercion = models.IntegerField(blank=True, null=True)
    capability = models.IntegerField(blank=True, null=True)
    compassion = models.IntegerField(blank=True, null=True)
    creativity = models.IntegerField(blank=True, null=True)
    courage = models.IntegerField(blank=True, null=True)
    corruption = models.TextField(blank=True, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True, related_name='character_location')
    titles = models.TextField(blank=True, null=True)
    institutions = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    family = models.TextField(blank=True, null=True)
    friends = models.TextField(blank=True, null=True)
    rivals = models.TextField(blank=True, null=True)
    relations = models.TextField(blank=True, null=True)
    hit_points = models.IntegerField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # 'class' is a reserved keyword in Python, hence the use of 'class_field'
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
    birthplace = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True, related_name='character_birthplace')
    objects = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    collectives = models.TextField(blank=True, null=True)
    backstory = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Institution(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    parent_institution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='child_institutions')
    image_url = models.TextField(blank=True, null=True)
    wealth = models.IntegerField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    cooperates = models.TextField(blank=True, null=True)
    members = models.TextField(blank=True, null=True)
    collectives = models.TextField(blank=True, null=True)
    basis = models.TextField(blank=True, null=True)
    dominion = models.TextField(blank=True, null=True)
    locations = models.TextField(blank=True, null=True)
    objects = models.TextField(blank=True, null=True)
    founding = models.TextField(blank=True, null=True)
    constructs = models.TextField(blank=True, null=True)
    phenomena = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    territories = models.TextField(blank=True, null=True)
    creatures = models.TextField(blank=True, null=True)
    legal = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)
    titles = models.TextField(blank=True, null=True)
    author = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='authored_institutions')


class Family(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    genealogy = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    members = models.TextField(blank=True, null=True)
    ambition = models.TextField(blank=True, null=True)
    founder = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True, related_name='founded_families')
    structure = models.TextField(blank=True, null=True)
    alliances = models.TextField(blank=True, null=True)
    rivalries = models.TextField(blank=True, null=True)
    estate = models.TextField(blank=True, null=True)
    holdings = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)


class Species(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    life_span = models.IntegerField(blank=True, null=True)
    average_weight = models.IntegerField(blank=True, null=True)
    appearance = models.TextField(blank=True, null=True)
    habitats = models.TextField(blank=True, null=True)
    agency = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    aggression = models.IntegerField(blank=True, null=True)
    consumption = models.TextField(blank=True, null=True)
    prey = models.TextField(blank=True, null=True)
    predators = models.TextField(blank=True, null=True)
    instincts = models.TextField(blank=True, null=True)
    behaviour = models.TextField(blank=True, null=True)



# Creature model
class Creature(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    institutions = models.TextField(blank=True, null=True)
    collectives = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    demeanour = models.TextField(blank=True, null=True)
    life_style = models.TextField(blank=True, null=True)
    territory = models.ForeignKey('Territory', on_delete=models.SET_NULL, blank=True, null=True, related_name='creatures')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True, related_name='resident_creatures')
    behaviour = models.TextField(blank=True, null=True)
    species = models.ForeignKey('Species', on_delete=models.SET_NULL, blank=True, null=True, related_name='creatures')
    creatures = models.TextField(blank=True, null=True)
    physicality = models.TextField(blank=True, null=True)
    lore = models.TextField(blank=True, null=True)
    senses = models.TextField(blank=True, null=True)
    hit_points = models.IntegerField(blank=True, null=True)
    armor_class = models.IntegerField(blank=True, null=True)
    challenge_rating = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    tt_str = models.IntegerField(blank=True, null=True)
    tt_int = models.IntegerField(blank=True, null=True)
    tt_con = models.IntegerField(blank=True, null=True)
    tt_dex = models.IntegerField(blank=True, null=True)
    tt_wis = models.IntegerField(blank=True, null=True)
    tt_cha = models.IntegerField(blank=True, null=True)
    languages = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)
    actions = models.TextField(blank=True, null=True)
    reactions = models.TextField(blank=True, null=True)
    alignment = models.TextField(blank=True, null=True)


# Collective model
class Collective(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    operator = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='operated_collectives')
    amount = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    formation_date = models.IntegerField(blank=True, null=True)
    temperance = models.TextField(blank=True, null=True)
    creatures = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)
    phenomena = models.TextField(blank=True, null=True)
    holdings = models.TextField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    rituals = models.TextField(blank=True, null=True)


class Trait(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    charisma = models.IntegerField(blank=True, null=True)
    coercion = models.IntegerField(blank=True, null=True)
    capability = models.IntegerField(blank=True, null=True)
    chastity = models.IntegerField(blank=True, null=True)
    creativity = models.IntegerField(blank=True, null=True)
    courage = models.IntegerField(blank=True, null=True)
    compassion = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    physical_effects = models.TextField(blank=True, null=True)
    mental_effects = models.TextField(blank=True, null=True)
    behaviour_effects = models.TextField(blank=True, null=True)
    ability_effects = models.TextField(blank=True, null=True)
    character_carriers = models.TextField(blank=True, null=True)
    creature_carriers = models.TextField(blank=True, null=True)
    antithesis_trait = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='antithesis_for')


class Phenomenon(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    origins = models.TextField(blank=True, null=True)
    catalyst = models.ForeignKey('Object', on_delete=models.SET_NULL, blank=True, null=True, related_name='phenomena')
    manifesters = models.TextField(blank=True, null=True)
    effect = models.TextField(blank=True, null=True)
    intensity = models.TextField(blank=True, null=True)
    triggers = models.TextField(blank=True, null=True)
    environments = models.TextField(blank=True, null=True)
    visibility = models.TextField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)




class Title(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    character = models.ForeignKey('Character', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    construct = models.ForeignKey('Construct', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    collective = models.ForeignKey('Collective', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    territory = models.ForeignKey('Territory', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    image_url = models.TextField(blank=True, null=True)
    creature = models.ForeignKey('Creature', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    object = models.ForeignKey('Object', on_delete=models.SET_NULL, blank=True, null=True, related_name='titles')
    create_date = models.IntegerField(blank=True, null=True)
    assign_date = models.IntegerField(blank=True, null=True)
    revoke_date = models.IntegerField(blank=True, null=True)
    privileges = models.TextField(blank=True, null=True)
    authority = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    hierarchy = models.IntegerField(blank=True, null=True)
    laws = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    author = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='authored_titles')



class Ability(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    is_magic = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    effects = models.TextField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    trait = models.ForeignKey('Trait', on_delete=models.SET_NULL, blank=True, null=True, related_name='abilities')
    carriers = models.TextField(blank=True, null=True)
    difficulty = models.TextField(blank=True, null=True)
    enablers = models.TextField(blank=True, null=True)
    prevalence = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)


class Language(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    spread = models.IntegerField(blank=True, null=True)
    prose = models.TextField(blank=True, null=True)
    writing = models.TextField(blank=True, null=True)
    phonology = models.TextField(blank=True, null=True)
    grammar = models.TextField(blank=True, null=True)
    vocabulary = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    dialects = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)
    species = models.TextField(blank=True, null=True)


class Law(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    prohibitions = models.TextField(blank=True, null=True)
    jurisdictions = models.TextField(blank=True, null=True)
    decree = models.TextField(blank=True, null=True)
    legalese = models.TextField(blank=True, null=True)
    employers = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    adjudicators = models.TextField(blank=True, null=True)
    enforcers = models.TextField(blank=True, null=True)
    penalties = models.TextField(blank=True, null=True)
    author = models.ForeignKey('Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='authored_laws')


class Relation(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    primary_character = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='primary_relations', blank=True, null=True)
    primary_institution = models.ForeignKey('Institution', on_delete=models.CASCADE, related_name='primary_institution_relations', blank=True, null=True)
    secondary_characters = models.TextField(blank=True, null=True)
    secondary_institutions = models.TextField(blank=True, null=True)
    debt = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    primary_creature = models.ForeignKey('Creature', on_delete=models.CASCADE, related_name='primary_creature_relations', blank=True, null=True)
    secondary_creatures = models.TextField(blank=True, null=True)  # Consider ManyToManyField for actual relationships
    impacts = models.TextField(blank=True, null=True)
    nature = models.TextField(blank=True, null=True)


class Event(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.TextField(blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)
    timestate = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    proceedings = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    background = models.TextField(blank=True, null=True)
    adversity = models.TextField(blank=True, null=True)
    consequences = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Character model
    objects = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Object model
    locations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Location model
    species = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Species model
    creatures = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Creature model
    institutions = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Institution model
    traits = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Trait model
    collectives = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Collective model
    territories = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Territory model
    abilities = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Ability model
    phenomena = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Phenomenon model
    languages = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Language model
    families = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Family model
    relations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Relation model
    titles = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Title model
    constructs = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Construct model


class Construct(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    supertype = models.ForeignKey('ConstructTyping', on_delete=models.CASCADE, related_name='constructs', blank=True, null=True)
    subtype = models.TextField(blank=True, null=True)  # This could link to a 'subtypes' field if defined in ConstructTyping
    image_url = models.TextField(blank=True, null=True)
    origin = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    characters = models.TextField(blank=True, null=True)  # Consider ManyToManyField if linking directly to Character models
    objects = models.TextField(blank=True, null=True)  # Consider ManyToManyField if linking directly to Object models
    locations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Location models
    creatures = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Creature models
    institutions = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Institution models
    relevance = models.TextField(blank=True, null=True)
    founder = models.ForeignKey('Character', on_delete=models.CASCADE, related_name='founded_constructs', blank=True, null=True)
    organiser = models.ForeignKey('Institution', on_delete=models.CASCADE, related_name='organised_constructs', blank=True, null=True)
    species = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Species models
    traits = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Trait models
    collectives = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Collective models
    territories = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Territory models
    abilities = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Ability models
    phenomena = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Phenomenon models
    languages = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Language models
    families = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Family models
    relations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Relation models
    titles = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Title models
    constructs = models.TextField(blank=True, null=True)  # For self-referencing constructs, consider a ManyToManyField


class World(models.Model):
    id = models.TextField(primary_key=True)
    ow_version = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_id = models.TextField(blank=True, null=True)  # Assuming this links to a user model or identification system
    image_url = models.TextField(blank=True, null=True)
    api_key = models.TextField(blank=True, null=True)
    world_time_state = models.TextField(blank=True, null=True)
    # The following fields could be JSON fields or ManyToManyFields if they're meant to store arrays of entities
    ability_string = models.TextField(blank=True, null=True)
    character_string = models.TextField(blank=True, null=True)
    collective_string = models.TextField(blank=True, null=True)
    construct_string = models.TextField(blank=True, null=True)
    creature_string = models.TextField(blank=True, null=True)
    event_string = models.TextField(blank=True, null=True)
    family_string = models.TextField(blank=True, null=True)
    phenomenon_string = models.TextField(blank=True, null=True)
    institution_string = models.TextField(blank=True, null=True)
    language_string = models.TextField(blank=True, null=True)
    law_string = models.TextField(blank=True, null=True)
    location_string = models.TextField(blank=True, null=True)
    map_string = models.TextField(blank=True, null=True)
    object_string = models.TextField(blank=True, null=True)
    pin_string = models.TextField(blank=True, null=True)
    species_string = models.TextField(blank=True, null=True)
    relation_string = models.TextField(blank=True, null=True)
    territory_string = models.TextField(blank=True, null=True)
    title_string = models.TextField(blank=True, null=True)
    trait_string = models.TextField(blank=True, null=True)
    family_grouping = models.TextField(blank=True, null=True)
    ability_grouping = models.TextField(blank=True, null=True)
    character_grouping = models.TextField(blank=True, null=True)
    collective_grouping = models.TextField(blank=True, null=True)
    construct_grouping = models.TextField(blank=True, null=True)
    creature_grouping = models.TextField(blank=True, null=True)
    event_grouping = models.TextField(blank=True, null=True)
    phenomenon_grouping = models.TextField(blank=True, null=True)
    institution_grouping = models.TextField(blank=True, null=True)
    language_grouping = models.TextField(blank=True, null=True)
    law_grouping = models.TextField(blank=True, null=True)
    location_grouping = models.TextField(blank=True, null=True)
    map_grouping = models.TextField(blank=True, null=True)
    object_grouping = models.TextField(blank=True, null=True)
    pin_grouping = models.TextField(blank=True, null=True)
    species_grouping = models.TextField(blank=True, null=True)
    relation_grouping = models.TextField(blank=True, null=True)
    territory_grouping = models.TextField(blank=True, null=True)
    title_grouping = models.TextField(blank=True, null=True)
    trait_grouping = models.TextField(blank=True, null=True)
    focus_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name