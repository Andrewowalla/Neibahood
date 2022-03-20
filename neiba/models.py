from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    # admin = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='hood')
    logo = CloudinaryField("image")
    description = models.TextField()
    health_no = models.IntegerField(null=True, blank=True)
    police_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)