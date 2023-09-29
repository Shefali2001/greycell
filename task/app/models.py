from django.db import models

# Create your models here.
class Intro(models.Model):
  name = models.CharField(max_length=150)
  email = models.EmailField()
  contact = models.PositiveBigIntegerField(null=True)
  age = models.PositiveBigIntegerField(null=True)

  class Meta:
    db_table = 'intro'
