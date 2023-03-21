from django.db import models

class StatusMixin(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    status=models.BooleanField(default=True)

    class Meta:
        abstract=True