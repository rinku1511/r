from django.contrib import admin

# Register your models here.
from .models import Reg,Person,contact,Donor,Supportus,Vol
admin.site.register(Reg)
admin.site.register(Person)
admin.site.register(contact)
admin.site.register(Donor)
admin.site.register(Vol)
admin.site.register(Supportus)