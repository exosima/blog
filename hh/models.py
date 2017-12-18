from django.db import models

# Create your models here.
class po(models.Model) :
 id = models.AutoField(primary_key=True)
 context = models.TextField(max_length=5000)
