from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ReminderThings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=250)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'reminder thingss'
        verbose_name_plural = 'reminder Things'

    def __str__(self):
        return self.title + " - " + str(self.id)
    