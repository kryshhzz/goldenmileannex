from django.contrib import admin

# Register your models here.
from import_export.admin import ExportActionMixin
from .models import *

class KmiAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email' )

class eAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email' )

class PavAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email' )

admin.site.register(keep_me_interested,KmiAdmin)
admin.site.register(enquiry,eAdmin)
admin.site.register(plan_a_visit,PavAdmin)