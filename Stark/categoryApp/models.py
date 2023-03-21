from django.db import models
from utils.utils import StatusMixin

class Category(StatusMixin):
    category_name=models.CharField(max_length=10,null=True,default=None)
    category_description=models.CharField(max_length=10,null=True,default=None)
