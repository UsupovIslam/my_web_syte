from django.db import models

class Fruits(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    img = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фрукт'
        verbose_name_plural = 'Фрукты'
