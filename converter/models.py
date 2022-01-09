from django.db import models


# Our currency pairing model.
class Pairing(models.Model):
    pairing = models.CharField(max_length=10)
    rate = models.FloatField()

    # DateTime automatically gets updated on every save_to_db() call.
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pairing
