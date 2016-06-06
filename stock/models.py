from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class ItemType(models.Model):
    type_name = models.CharField(max_length=255)
    type_notes = models.TextField()
    
    class Meta:
        verbose_name_plural = "Item Types"
    
    def __str__(self):
        return self.type_name
    
    
class Color(models.Model):
    color_name = models.CharField(max_length=255)
    type_notes = models.TextField()
    
    def __str__(self):
        return self.color_name  
    

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    weight = models.FloatField(null=True)
    photo = models.FileField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    itemType = models.ForeignKey(ItemType)
    color = models.ForeignKey(Color, null=True)
    
    class Meta:
        verbose_name_plural = "Inventories"        
        
    def get_absolute_url(self):
        return reverse('stock:details', kwargs={
            'pk': self.id
        })        
    
    def __str__(self):
        return self.name
    