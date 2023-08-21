from django.contrib import admin
from core.models import *
# Register your models here.



@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameters','updated_date','created_date',]
    search_fields = ['name','description','parameters',]
    list_editable = ['description','parameters',]
    class Meta:
        model = GeneralSetting
@admin.register(ImageSettings)
class ImageSettings(admin.ModelAdmin):
    list_display = ['name', 'description','updated_date','created_date','file']
    search_fields = ['name', 'description',]
    list_editable = ['description']
    class Meta:
        model =ImageSettings





