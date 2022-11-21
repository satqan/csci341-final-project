from django.db import models


class Disease(models.Model):
    disease_code = models.CharField(
        max_length=50,
        primary_key=True
    )
    pathogen = models.CharField(
        max_length=20
    )
    description = models.CharField(
        max_length=140
    )
    id = models.ForeignKey(
        'DiseaseType.DiseaseType',
        related_name='diseases',
        on_delete=models.CASCADE,
    )

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Disease._meta.fields]
