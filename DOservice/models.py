from django.db import models

# Create your models here.
class DesignPiece(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title