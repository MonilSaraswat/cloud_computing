from django.db import models


# Create your models here.
class UploadedImages(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    name = models.CharField(db_index=True, blank=False, null=False, max_length=100)
    type = models.CharField(db_index=True, blank=False, null=False, max_length=50)
    aws_path = models.CharField(db_index=True, blank=False, null=False, max_length=450)
    size = models.CharField(db_index=True, blank=False, null=False, max_length=100)
    end_point = models.CharField(db_index=True, blank=False, null=False, max_length=100)

