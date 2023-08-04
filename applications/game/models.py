from django.db import models
import uuid

class GameDB(models.Model):
    world = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)
    history = models.JSONField()
    is_win = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.world}"
