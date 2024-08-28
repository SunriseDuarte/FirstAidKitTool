from django.contrib import admin
from .models import Location, Boxtyp, Boxitem, Inventuritem, Inventur

# Register your models here.
admin.site.register(Location)
admin.site.register(Boxtyp)
admin.site.register(Boxitem)
admin.site.register(Inventuritem)
admin.site.register(Inventur)

