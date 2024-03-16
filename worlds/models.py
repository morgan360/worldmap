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


# WITH base model
class Character(BaseModel):
    appearance = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    traits = models.TextField(blank=True, null=True)

class Location(BaseModel):
    population = models.TextField(blank=True, null=True)
    population_size = models.IntegerField(blank=True, null=True)
    parent_location = models.TextField(blank=True, null=True)
    founded_by = models.TextField(blank=True, null=True)
    maps = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)

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


# WITHOUT base model

# class Character(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     appearance = models.TextField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#     traits = models.TextField(blank=True, null=True)
#
# class Location(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     population = models.TextField(blank=True, null=True)
#     population_size = models.IntegerField(blank=True, null=True)
#     parent_location = models.TextField(blank=True, null=True)
#     founded_by = models.TextField(blank=True, null=True)
#     maps = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#
# class Object(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     aesthetics = models.TextField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     parent_object = models.TextField(blank=True, null=True)
#     technology = models.TextField(blank=True, null=True)
#     components = models.TextField(blank=True, null=True)
#
# class Creature(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     physicality = models.TextField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#
# class Institution(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     basis = models.TextField(blank=True, null=True)
#     parent_institution = models.TextField(blank=True, null=True)
#     creatures = models.TextField(blank=True, null=True)








# FULL


# class Location(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     institution_owner = models.TextField(blank=True, null=True)
#     character_owner =models.TextField(blank=True, null=True)
#     coordinates = models.TextField(blank=True, null=True)
#     parent_location = models.TextField(blank=True, null=True)
#     maps = models.TextField(blank=True, null=True)
#     pins = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     founded_by = models.TextField(blank=True, null=True)
#     primary_faction = models.TextField(blank=True, null=True)
#     secondary_factions = models.TextField(blank=True, null=True)
#     population_size = models.IntegerField(blank=True, null=True)
#     government_description = models.TextField(blank=True, null=True)
#     hard_influence_on = models.TextField(blank=True, null=True)
#     soft_influence_on = models.TextField(blank=True, null=True)
#     rival = models.TextField(blank=True, null=True)
#     friend = models.TextField(blank=True, null=True)
#     government = models.TextField(blank=True, null=True)
#     opposition = models.TextField(blank=True, null=True)
#     regional_character = models.TextField(blank=True, null=True)
#     primary_resource = models.TextField(blank=True, null=True)
#     secondary_resources = models.TextField(blank=True, null=True)
#     primary_industry = models.TextField(blank=True, null=True)
#     secondary_industries = models.TextField(blank=True, null=True)
#     generation_rate = models.TextField(blank=True, null=True)
#     industry_rate = models.TextField(blank=True, null=True)
#     construction_rate = models.TextField(blank=True, null=True)
#     primary_generation_offload = models.TextField(blank=True, null=True)
#     primary_industry_offload = models.TextField(blank=True, null=True)
#     secondary_generation_offloads = models.TextField(blank=True, null=True)
#     secondary_industry_offloads = models.TextField(blank=True, null=True)
#     coinage = models.TextField(blank=True, null=True)
#     logistics = models.TextField(blank=True, null=True)
#     harbor = models.TextField(blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     natural_defenses = models.TextField(blank=True, null=True)
#     fortifications = models.TextField(blank=True, null=True)
#     primary_fighter = models.TextField(blank=True, null=True)
#     secondary_fighters = models.TextField(blank=True, null=True)
#     primary_cult = models.TextField(blank=True, null=True)
#     secondary_cults = models.TextField(blank=True, null=True)
#     founding_date = models.IntegerField(blank=True, null=True)
#     population = models.TextField(blank=True, null=True)
#     position = models.TextField(blank=True, null=True)
#     collectives = models.TextField(blank=True, null=True)
#     economics = models.TextField(blank=True, null=True)
#     architecture = models.TextField(blank=True, null=True)
#     commerce = models.TextField(blank=True, null=True)
#     territory = models.TextField(blank=True, null=True)
#     defensibility = models.TextField(blank=True, null=True)
#     culture = models.TextField(blank=True, null=True)
#     religion = models.TextField(blank=True, null=True)
#     delicacies = models.TextField(blank=True, null=True)
#     buildings = models.TextField(blank=True, null=True)
#     building_expertise = models.TextField(blank=True, null=True)
#     places = models.TextField(blank=True, null=True)
#     governing_title = models.TextField(blank=True, null=True)
#
#
#
# class Object(BaseModel):
#     category = models.TextField(blank=True, null=True)
#     amount = models.IntegerField(blank=True, null=True)
#     weight =  models.IntegerField(blank=True, null=True)
#     value =  models.IntegerField(blank=True, null=True)
#     value_per_weight =  models.IntegerField(blank=True, null=True)
#     institution = models.TextField(blank=True, null=True)
#     character = models.TextField(blank=True, null=True)
#     parent_object =models.TextField(blank=True, null=True)
#     components = models.TextField(blank=True, null=True)
#     rarity = models.TextField(blank=True, null=True)
#     background = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
# class Territory(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     yield_rate = models.IntegerField(blank=True, null=True)
#     terrain = models.TextField(blank=True, null=True)
#     locations = models.TextField(blank=True, null=True)
#     history = models.TextField(blank=True, null=True)
#     claimants = models.TextField(blank=True, null=True)
#     creatures = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#     phenomena = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#     conditions = models.TextField(blank=True, null=True)
#     primary_resource = models.TextField(blank=True, null=True)
#     secondary_resources = models.TextField(blank=True, null=True)
#     parent_territory = models.TextField(blank=True, null=True)
#     sub_territories = models.TextField(blank=True, null=True)
#     def __str__(self):
#         return self.name
#
#
#
# class Character(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     gender = models.TextField(blank=True, null=True)
#     physicality = models.TextField(blank=True, null=True)
#     traits = models.TextField(blank=True, null=True)
#     languages = models.TextField(blank=True, null=True)
#     abilities = models.TextField(blank=True, null=True)
#     appearance = models.TextField(blank=True, null=True)
#     background = models.TextField(blank=True, null=True)
#     motivations = models.TextField(blank=True, null=True)
#     situation = models.TextField(blank=True, null=True)
#     charisma = models.IntegerField(blank=True, null=True)
#     coercion = models.IntegerField(blank=True, null=True)
#     capability = models.IntegerField(blank=True, null=True)
#     compassion = models.IntegerField(blank=True, null=True)
#     creativity = models.IntegerField(blank=True, null=True)
#     courage = models.IntegerField(blank=True, null=True)
#     corruption = models.TextField(blank=True, null=True)
#     location =  models.TextField(blank=True, null=True)
#     titles = models.TextField(blank=True, null=True)
#     institutions = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#     family = models.TextField(blank=True, null=True)
#     friends = models.TextField(blank=True, null=True)
#     rivals = models.TextField(blank=True, null=True)
#     relations = models.TextField(blank=True, null=True)
#     hit_points = models.IntegerField(blank=True, null=True)
#     class_field = models.TextField(db_column='class', blank=True, null=True) #@not sure if this works, otherwise can rename the column
#     alignment = models.TextField(blank=True, null=True)
#     inspirations = models.TextField(blank=True, null=True)
#     tt_str = models.IntegerField(blank=True, null=True)
#     tt_int = models.IntegerField(blank=True, null=True)
#     tt_con = models.IntegerField(blank=True, null=True)
#     tt_dex = models.IntegerField(blank=True, null=True)
#     tt_wis = models.IntegerField(blank=True, null=True)
#     tt_cha = models.IntegerField(blank=True, null=True)
#     skill_stealth = models.IntegerField(blank=True, null=True)
#     equipment = models.TextField(blank=True, null=True)
#     backpack = models.TextField(blank=True, null=True)
#     proficiencies = models.TextField(blank=True, null=True)
#     features = models.TextField(blank=True, null=True)
#     spells = models.TextField(blank=True, null=True)
#     birthplace = models.TextField(blank=True, null=True)
#     objects = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#     collectives = models.TextField(blank=True, null=True)
#     backstory = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name
#
# class Institution(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     parent_institution = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     wealth = models.IntegerField(blank=True, null=True)
#     background = models.TextField(blank=True, null=True)
#     cooperates = models.TextField(blank=True, null=True)
#     members = models.TextField(blank=True, null=True)
#     collectives = models.TextField(blank=True, null=True)
#     basis = models.TextField(blank=True, null=True)
#     dominion = models.TextField(blank=True, null=True)
#     locations = models.TextField(blank=True, null=True)
#     objects = models.TextField(blank=True, null=True)
#     founding = models.TextField(blank=True, null=True)
#     constructs = models.TextField(blank=True, null=True)
#     phenomena = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#     territories = models.TextField(blank=True, null=True)
#     creatures = models.TextField(blank=True, null=True)
#     legal = models.TextField(blank=True, null=True)
#     characters = models.TextField(blank=True, null=True)
#     titles = models.TextField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#
#
# class Family(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     genealogy = models.TextField(blank=True, null=True)
#     history = models.TextField(blank=True, null=True)
#     members = models.TextField(blank=True, null=True)
#     ambition = models.TextField(blank=True, null=True)
#     founder = models.TextField(blank=True, null=True)
#     structure = models.TextField(blank=True, null=True)
#     alliances = models.TextField(blank=True, null=True)
#     rivalries = models.TextField(blank=True, null=True)
#     estate = models.TextField(blank=True, null=True)
#     holdings = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#
#
# class Species(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     life_span = models.IntegerField(blank=True, null=True)
#     average_weight = models.IntegerField(blank=True, null=True)
#     appearance = models.TextField(blank=True, null=True)
#     habitats = models.TextField(blank=True, null=True)
#     agency = models.TextField(blank=True, null=True)
#     traits = models.TextField(blank=True, null=True)
#     languages = models.TextField(blank=True, null=True)
#     aggression = models.IntegerField(blank=True, null=True)
#     consumption = models.TextField(blank=True, null=True)
#     prey = models.TextField(blank=True, null=True)
#     predators = models.TextField(blank=True, null=True)
#     instincts = models.TextField(blank=True, null=True)
#     behaviour = models.TextField(blank=True, null=True)
#
#
#
# # Creature model
# class Creature(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     institutions = models.TextField(blank=True, null=True)
#     collectives = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     abilities = models.TextField(blank=True, null=True)
#     demeanour = models.TextField(blank=True, null=True)
#     life_style = models.TextField(blank=True, null=True)
#     territory =  models.TextField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#     instincts = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#     creatures = models.TextField(blank=True, null=True)
#     appearance = models.TextField(blank=True, null=True)
#     lore = models.TextField(blank=True, null=True)
#     senses = models.TextField(blank=True, null=True)
#     hit_points = models.IntegerField(blank=True, null=True)
#     armor_class = models.IntegerField(blank=True, null=True)
#     challenge_rating = models.IntegerField(blank=True, null=True)
#     speed = models.IntegerField(blank=True, null=True)
#     tt_str = models.IntegerField(blank=True, null=True)
#     tt_int = models.IntegerField(blank=True, null=True)
#     tt_con = models.IntegerField(blank=True, null=True)
#     tt_dex = models.IntegerField(blank=True, null=True)
#     tt_wis = models.IntegerField(blank=True, null=True)
#     tt_cha = models.IntegerField(blank=True, null=True)
#     languages = models.TextField(blank=True, null=True)
#     traits = models.TextField(blank=True, null=True)
#     actions = models.TextField(blank=True, null=True)
#     reactions = models.TextField(blank=True, null=True)
#     alignment = models.TextField(blank=True, null=True)
#
# # Collective model
# class Collective(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     operator =  models.TextField(blank=True, null=True)
#     amount = models.IntegerField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     characters = models.TextField(blank=True, null=True)
#     background = models.TextField(blank=True, null=True)
#     formation_date = models.IntegerField(blank=True, null=True)
#     temperance = models.TextField(blank=True, null=True)
#     creatures = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#     phenomena = models.TextField(blank=True, null=True)
#     holdings = models.TextField(blank=True, null=True)
#     activity = models.TextField(blank=True, null=True)
#     rituals = models.TextField(blank=True, null=True)
#
#
# class Trait(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     charisma = models.IntegerField(blank=True, null=True)
#     coercion = models.IntegerField(blank=True, null=True)
#     capability = models.IntegerField(blank=True, null=True)
#     chastity = models.IntegerField(blank=True, null=True)
#     creativity = models.IntegerField(blank=True, null=True)
#     courage = models.IntegerField(blank=True, null=True)
#     compassion = models.IntegerField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     physical_effects = models.TextField(blank=True, null=True)
#     mental_effects = models.TextField(blank=True, null=True)
#     behaviour_effects = models.TextField(blank=True, null=True)
#     ability_effects = models.TextField(blank=True, null=True)
#     character_carriers = models.TextField(blank=True, null=True)
#     creature_carriers = models.TextField(blank=True, null=True)
#     anti_trait =  models.TextField(blank=True, null=True)
#     empowered_abilities = models.TextField(blank=True, null=True)
#
#
# class Phenomenon(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     duration = models.IntegerField(blank=True, null=True)
#     origins = models.TextField(blank=True, null=True)
#     catalysts =models.TextField(blank=True, null=True)
#     manifesters = models.TextField(blank=True, null=True)
#     effect = models.TextField(blank=True, null=True)
#     intensity = models.TextField(blank=True, null=True)
#     triggers = models.TextField(blank=True, null=True)
#     environments = models.TextField(blank=True, null=True)
#     visibility = models.TextField(blank=True, null=True)
#     scope = models.TextField(blank=True, null=True)
#     enablers = models.TextField(blank=True, null=True)
#
#
#
#
# class Title(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     character =  models.TextField(blank=True, null=True)
#     construct =  models.TextField(blank=True, null=True)
#     institution = models.TextField(blank=True, null=True)
#     collective =  models.TextField(blank=True, null=True)
#     territory =  models.TextField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     creature =  models.TextField(blank=True, null=True)
#     object =  models.TextField(blank=True, null=True)
#     create_date = models.IntegerField(blank=True, null=True)
#     assign_date = models.IntegerField(blank=True, null=True)
#     revoke_date = models.IntegerField(blank=True, null=True)
#     privileges = models.TextField(blank=True, null=True)
#     authority = models.TextField(blank=True, null=True)
#     conditions = models.TextField(blank=True, null=True)
#     hierarchy = models.IntegerField(blank=True, null=True)
#     laws = models.TextField(blank=True, null=True)
#     events = models.TextField(blank=True, null=True)
#     author =  models.TextField(blank=True, null=True)
#
#
#
# class Ability(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     is_magic = models.IntegerField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     range = models.IntegerField(blank=True, null=True)
#     effects = models.TextField(blank=True, null=True)
#     strength = models.IntegerField(blank=True, null=True)
#     trait =  models.TextField(blank=True, null=True)
#     carriers = models.TextField(blank=True, null=True)
#     difficulty = models.TextField(blank=True, null=True)
#     enablers = models.TextField(blank=True, null=True)
#     prevalence = models.TextField(blank=True, null=True)
#     origin = models.TextField(blank=True, null=True)
#     usage = models.TextField(blank=True, null=True)
#
#
# class Language(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     spread = models.IntegerField(blank=True, null=True)
#     prose = models.TextField(blank=True, null=True)
#     writing = models.TextField(blank=True, null=True)
#     phonology = models.TextField(blank=True, null=True)
#     grammar = models.TextField(blank=True, null=True)
#     vocabulary = models.TextField(blank=True, null=True)
#     classification = models.TextField(blank=True, null=True)
#     dialects = models.TextField(blank=True, null=True)
#     range = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)
#
#
# class Law(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     date = models.IntegerField(blank=True, null=True)
#     prohibitions = models.TextField(blank=True, null=True)
#     jurisdictions = models.TextField(blank=True, null=True)
#     decree = models.TextField(blank=True, null=True)
#     legalese = models.TextField(blank=True, null=True)
#     employers = models.TextField(blank=True, null=True)
#     purpose = models.TextField(blank=True, null=True)
#     adjudicators = models.TextField(blank=True, null=True)
#     enforcers = models.TextField(blank=True, null=True)
#     penalties = models.TextField(blank=True, null=True)
#     author = models.TextField(blank=True, null=True)
#
#
# class Relation(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     primary_character =  models.TextField(blank=True, null=True)
#     primary_institution =  models.TextField(blank=True, null=True)
#     secondary_characters = models.TextField(blank=True, null=True)
#     secondary_institutions = models.TextField(blank=True, null=True)
#     debt = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     primary_creature = models.TextField(blank=True, null=True)
#     secondary_creatures = models.TextField(blank=True, null=True)
#     impacts = models.TextField(blank=True, null=True)
#     nature = models.TextField(blank=True, null=True)
#
#
# class Event(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype = models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     timestate = models.IntegerField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     proceedings = models.TextField(blank=True, null=True)
#     history = models.TextField(blank=True, null=True)
#     background = models.TextField(blank=True, null=True)
#     adversity = models.TextField(blank=True, null=True)
#     consequences = models.TextField(blank=True, null=True)
#     characters = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Character model
#     objects = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Object model
#     locations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Location model
#     species = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Species model
#     creatures = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Creature model
#     institutions = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Institution model
#     traits = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Trait model
#     collectives = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Collective model
#     territories = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Territory model
#     abilities = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Ability model
#     phenomena = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Phenomenon model
#     languages = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Language model
#     families = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Family model
#     relations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Relation model
#     titles = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Title model
#     constructs = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Construct model
#
#
# class Construct(models.Model):
#     id = models.TextField(primary_key=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     supertype =  models.TextField(blank=True, null=True)
#     subtype = models.TextField(blank=True, null=True)
#     image_url = models.TextField(blank=True, null=True)
#     origin = models.TextField(blank=True, null=True)
#     state = models.TextField(blank=True, null=True)
#     characters = models.TextField(blank=True, null=True)  # Consider ManyToManyField if linking directly to Character models
#     objects = models.TextField(blank=True, null=True)  # Consider ManyToManyField if linking directly to Object models
#     locations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Location models
#     creatures = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Creature models
#     institutions = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Institution models
#     relevance = models.TextField(blank=True, null=True)
#     founder =  models.TextField(blank=True, null=True)
#     organiser = models.TextField(blank=True, null=True)
#     species = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Species models
#     traits = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Trait models
#     collectives = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Collective models
#     territories = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Territory models
#     abilities = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Ability models
#     phenomena = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Phenomenon models
#     languages = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Language models
#     families = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Family models
#     relations = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Relation models
#     titles = models.TextField(blank=True, null=True)  # Consider ManyToManyField for linking to Title models
#     constructs = models.TextField(blank=True, null=True)  # For self-referencing constructs, consider a ManyToManyField
#
#
# class World(models.Model):
#     id = models.TextField(primary_key=True)
#     ow_version = models.TextField(blank=True, null=True)
#     name = models.TextField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     user_id = models.TextField(blank=True, null=True)  # Assuming this links to a user model or identification system
#     image_url = models.TextField(blank=True, null=True)
#     api_key = models.TextField(blank=True, null=True)
#     world_time_state = models.TextField(blank=True, null=True)
#     # The following fields could be JSON fields or ManyToManyFields if they're meant to store arrays of entities
#     ability_string = models.TextField(blank=True, null=True)
#     character_string = models.TextField(blank=True, null=True)
#     collective_string = models.TextField(blank=True, null=True)
#     construct_string = models.TextField(blank=True, null=True)
#     creature_string = models.TextField(blank=True, null=True)
#     event_string = models.TextField(blank=True, null=True)
#     family_string = models.TextField(blank=True, null=True)
#     phenomenon_string = models.TextField(blank=True, null=True)
#     institution_string = models.TextField(blank=True, null=True)
#     language_string = models.TextField(blank=True, null=True)
#     law_string = models.TextField(blank=True, null=True)
#     location_string = models.TextField(blank=True, null=True)
#     map_string = models.TextField(blank=True, null=True)
#     object_string = models.TextField(blank=True, null=True)
#     pin_string = models.TextField(blank=True, null=True)
#     species_string = models.TextField(blank=True, null=True)
#     relation_string = models.TextField(blank=True, null=True)
#     territory_string = models.TextField(blank=True, null=True)
#     title_string = models.TextField(blank=True, null=True)
#     trait_string = models.TextField(blank=True, null=True)
#     family_grouping = models.TextField(blank=True, null=True)
#     ability_grouping = models.TextField(blank=True, null=True)
#     character_grouping = models.TextField(blank=True, null=True)
#     collective_grouping = models.TextField(blank=True, null=True)
#     construct_grouping = models.TextField(blank=True, null=True)
#     creature_grouping = models.TextField(blank=True, null=True)
#     event_grouping = models.TextField(blank=True, null=True)
#     phenomenon_grouping = models.TextField(blank=True, null=True)
#     institution_grouping = models.TextField(blank=True, null=True)
#     language_grouping = models.TextField(blank=True, null=True)
#     law_grouping = models.TextField(blank=True, null=True)
#     location_grouping = models.TextField(blank=True, null=True)
#     map_grouping = models.TextField(blank=True, null=True)
#     object_grouping = models.TextField(blank=True, null=True)
#     pin_grouping = models.TextField(blank=True, null=True)
#     species_grouping = models.TextField(blank=True, null=True)
#     relation_grouping = models.TextField(blank=True, null=True)
#     territory_grouping = models.TextField(blank=True, null=True)
#     title_grouping = models.TextField(blank=True, null=True)
#     trait_grouping = models.TextField(blank=True, null=True)
#     focus_text = models.TextField(blank=True, null=True)
#     time_format_names = models.TextField(blank=True, null=True)
#     time_format_equivalents = models.TextField(blank=True, null=True)
#     time_default_format = models.TextField(blank=True, null=True)
#     time_current_value = models.IntegerField(blank=True, null=True)
#     time_range = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name