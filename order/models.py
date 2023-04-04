from django.db import models


class Status(models.Model):

    name = models.CharField(max_length=32)
    next_status = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        reveal_type(self.id) 
        reveal_type(self.name)
        reveal_type(self.next_status)
        reveal_type(self.order)
        return self.id