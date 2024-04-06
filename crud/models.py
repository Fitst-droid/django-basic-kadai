from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=200)
  explanation = models.TextField()
  price = models.PositiveIntegerField(null=True, blank=True)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  img = models.ImageField(blank=True, default='noImage.png')

  def __str__(self):
    return self.name
