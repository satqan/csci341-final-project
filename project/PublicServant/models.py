from django.db import models


class PublicServant(models.Model):
    email = models.OneToOneField(
        'Users.Users',
        related_name='public_servants',
        on_delete=models.CASCADE,
        primary_key=True
    )
    department = models.CharField(
        max_length=50
    )

    def get_fields(self):
        return [(field.name.capitalize().replace('_', ' '), field.value_to_string(self)) for field in PublicServant._meta.fields]
