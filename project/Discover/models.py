from django.db import models


class Discover(models.Model):
    cname = models.ForeignKey(
        'Country.Country',
        related_name='discovers',
        on_delete=models.CASCADE
    )
    disease_code = models.ForeignKey(
        'Disease.Disease',
        related_name='discovers',
        on_delete=models.CASCADE
    )
    first_enc_date = models.DateField()

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Discover._meta.fields]


    class Meta:
        unique_together = (('cname', 'disease_code'),)
