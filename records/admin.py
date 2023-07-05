from django.contrib import admin

# Register your models here.

from records.models import *

# admin.site.register(Clients)
admin.site.register(Methods)
admin.site.register(Events)
admin.site.register(Feelings)
# admin.site.register(Therapist)
# admin.site.register(Records)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email')
@admin.register(Records)
class RecordsAdmin(admin.ModelAdmin):
    list_display = ('therapist', 'client', 'date', 'price')