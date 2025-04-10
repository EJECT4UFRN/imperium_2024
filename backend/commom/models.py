from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street}, {self.number}, {self.city}, {self.state}"
    