from django.contrib import admin
from home.models import ExeltoData, AllData


class ExeltoDataAdmin(admin.ModelAdmin):
    list_display = ('DATE', 'INN', 'FIRMA', 'SUMDA', 'KURS', 'DOLLAR', 'ID', 'CLIENT', 'REGION', 'MANAGER')
    readonly_fields = ['ID']


class AllDataAdmin(admin.ModelAdmin):
    list_display = ('DATE', 'INN', 'FIRMA', 'SUMDA', 'KURS', 'DOLLAR', 'ID', 'CLIENT', 'REGION', 'MANAGER')
    readonly_fields = ['ID']


admin.site.register(AllData, AllDataAdmin)
admin.site.register(ExeltoData, ExeltoDataAdmin)
