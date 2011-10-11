from django.db import models
import time


TIMEOUT = 0.1


class FanState(models.Model):
    last_call = models.FloatField(default=0)
    available = models.BooleanField(default=False)
    speed = models.IntegerField(default=0)

    def update_availability(self):
        self.available = (time.time() - self.last_call) < TIMEOUT
