from django.db import models


class Doctor(models.Model):
    email = models.OneToOneField(
        'Users.Users',
        related_name='doctors',
        on_delete=models.CASCADE,
        primary_key=True
    )
    degree = models.CharField(
        max_length=20
    )

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in Doctor._meta.fields]

