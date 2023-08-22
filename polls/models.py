import datetime
from django.db import models
from django.utils import timezone
from datetime import datetime 
from django.contrib import admin
from django.utils.html import mark_safe

class Owner(models.Model):
    class Meta:
        verbose_name = 'Propietario'
        verbose_name_plural = 'Propietarios'

    identification = models.CharField(max_length=16)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.name
        
class Property(models.Model):
    class Meta:
        verbose_name = 'Inmueble'
        verbose_name_plural = 'Inmuebles'
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    number_property = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    def __str__(self):
        return self.number_property

class Aliquot(models.Model):
    class Meta:
        verbose_name = 'Alicuota'
        verbose_name_plural = 'Alicuotas'
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    value = models.IntegerField( null=True, blank=True)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    reference = models.CharField(max_length=128)
    def __str__(self):
        return self.reference

    
    
class OwnerAdmin(admin.ModelAdmin):
        list_display = ['identification','name', 'last_name','phone']
        list_filter = [ 'identification','name', 'last_name']
        search_fields = ['identification','name', 'last_name']
        fields = ['identification','name', 'last_name','phone']
class PropertyAdmin(admin.ModelAdmin):
        list_display = ['owner','number_property', 'phone','address']
        list_filter = [ 'owner','number_property']
        search_fields = ['owner','number_property']
        fields = ['owner','number_property', 'phone','address']
class AliquotAdmin(admin.ModelAdmin):
        list_display = ['property','value', 'month','year', 'description', 'reference']
        list_filter = [ 'reference']
        search_fields = ['reference']
        fields = ['property','value', 'month','year', 'description', 'reference']