from tortoise.models import Model
from tortoise import fields


class Films(Model):
    id = fields.IntField(pk=True)  # prob unique is extra
    title = fields.CharField(max_length=255)
    director = fields.CharField(max_length=255)
    year = fields.IntField()
    description = fields.CharField(max_length=1000)
    length = fields.IntField()
    rating = fields.CharField(max_length=255)
    categories: fields.ReverseRelation["Category"]
    cast: fields.ReverseRelation["FilmCast"]
    image: fields.ReverseRelation["Images"]


class Category(Model):
    category_name = fields.CharField(max_length=255, pk=True)
    film: fields.ForeignKeyRelation[Films] = \
        fields.ForeignKeyField("models.Films", related_name='categories')


class FilmCast(Model):
    actor_id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    film: fields.ForeignKeyRelation[Films] = fields.ForeignKeyField("models.Films", related_name='cast')

    class Meta:
        unique_together = ("actor_id", "film")


class Images(Model):
    id = fields.IntField(pk=True)
    image_url = fields.CharField(max_length=500)
    film: fields.ForeignKeyRelation[Films] = fields.ForeignKeyField("models.Films", related_name='image')
