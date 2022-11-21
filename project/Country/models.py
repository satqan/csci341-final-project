from django.db import models


class Country(models.Model):
    cname = models.CharField(
        max_length=50,
        primary_key=True
    )
    population = models.BigIntegerField()

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Country._meta.fields]
