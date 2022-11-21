from django.db import models


class Users(models.Model):
    email = models.CharField(
        max_length=60,
        primary_key=True
    )
    name = models.CharField(
        max_length=30
    )
    surname = models.CharField(
        max_length=40
    )
    salary = models.IntegerField()
    phone = models.CharField(
        max_length=20
    )
    cname = models.ForeignKey(
        'Country.Country',
        related_name='users',
        on_delete=models.CASCADE,
    )

    def get_fields(self):
        return [(field.name.capitalize(), field.value_to_string(self)) for field in Users._meta.fields]
