from django.db import models


class Status(models.Model):

    name = models.CharField(max_length=32)
    next_status = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name