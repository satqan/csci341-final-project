from django.db import models


class Specialize(models.Model):
    id = models.OneToOneField(
        'DiseaseType.DiseaseType',
        on_delete=models.CASCADE,
        related_name='specializations',
        primary_key=True
    )
    email = models.ForeignKey(
        'Doctor.Doctor',
        on_delete=models.CASCADE,
        related_name='specializations'
    )

    class Meta:
        unique_together = (('id', 'email'),)

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Specialize._meta.fields]
