from django.db import models


class Note(models.Model):
    text = models.TextField(default="")

    def __str__(self):
        return "{}: {}".format(self.id, self.text)
