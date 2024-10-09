from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
class Headline(models.Model):
  title = models.CharField(max_length=200)
  link = models.URLField(null=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.title