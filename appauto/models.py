from django.db import models

# Create your models here.
class Auto(models.Model):
    marca = models.CharField("marca",max_length=15, null=True, blank=True)
    modello = models.CharField("modello",max_length=15, null=True, blank=True)
    prezzo = models.IntegerField()
    km = models.IntegerField()
    anno = models.IntegerField()
    dettagli = models.CharField(max_length=255, null=True, blank=True)
    immagine = models.ImageField(upload_to='media')

def delete(self, *args, **kwargs):
    self.feature_image.delete()
    self.attachment.delete()
    super().delete(*args, **kwargs)

def __str__(self):
    return self.marca

