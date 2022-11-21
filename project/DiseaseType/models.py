from django.db import models
from django.utils.translation import gettext_lazy as _


class DiseaseType(models.Model):
    id = models.IntegerField(
        primary_key=True,
    )
    description = models.CharField(
        max_length=140
    )

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in DiseaseType._meta.fields]
