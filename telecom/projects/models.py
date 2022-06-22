from django.db import models
from users.models import Profile


# Create your models here.
class Service(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    Name = models.CharField(max_length=200)
    Price = models.FloatField(max_length=200)
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    Franchise = models.IntegerField(null=False,default=0)
    ExtraFranchise = models.IntegerField(default=0)
    ServiceType = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    Id = models.AutoField(primary_key=True, unique=True, 
                                             editable=False)
    
    def __str__(self):
        return self.Name
    
class Packets(models.Model):
    Name = models.CharField(max_length=200)
    MonthlyPayment = models.IntegerField(null=False, default=0)
    created = models.DateTimeField(auto_now_add=True)
    Id = models.AutoField(primary_key=True, unique=True, 
                                             editable=False)
    def __str__(self):
        return self.Name

class Packets_Services(models.Model):
    IdService = models.ForeignKey("Packets", on_delete=models.CASCADE, related_name='servico_fk')
    IdPackets = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='packets_fk')
    Id = models.AutoField(primary_key=True, unique=True, 
                                             editable=False)   