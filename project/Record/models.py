from django.db import models


class Record(models.Model):
    email = models.ForeignKey(
        'PublicServant.PublicServant',
        related_name='records',
        on_delete=models.CASCADE
    )
    cname = models.ForeignKey(
        'Country.Country',
        related_name='records',
        on_delete=models.CASCADE
    )
    disease_code = models.ForeignKey(
        'Disease.Disease',
        related_name='records',
        on_delete=models.CASCADE
    )
    total_deaths = models.IntegerField()
    total_patients = models.IntegerField()

    class Meta:
        unique_together = (('email', 'cname', 'disease_code'),)

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Record._meta.fields]
