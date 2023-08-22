from django.contrib import admin
from .models import Owner, Property, Aliquot, OwnerAdmin, AliquotAdmin, PropertyAdmin

admin.site.register(Owner, OwnerAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Aliquot, AliquotAdmin)