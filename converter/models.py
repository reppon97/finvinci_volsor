from django.db import models


class Pairing(models.Model):
    pairing = models.CharField(max_length=10)
    rate = models.FloatField()
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pairing
