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



@admin.register(Skill)
class Skill(admin.ModelAdmin):
    list_display = ['id', 'order','name','percentage','updated_date','created_date']
    search_fields = ['name']
    list_editable = ['order','name','percentage',]
    class Meta:
        model =Skill

@admin.register(Experience)
class Experience(admin.ModelAdmin):
    list_display = ['id', 'company_name','job_title','job_location','start_date','end_date','updated_date','created_date']
    search_fields = ['company_name','job_title']
    list_editable = ['company_name','job_title','job_location','start_date','end_date']
    class Meta:
        model =Experience

@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = ['id', 'school_name','major','department','start_date','end_date','updated_date','created_date']
    search_fields = ['school_name','major','department']
    list_editable = ['school_name','major','department','start_date','end_date']
    class Meta:
        model =Education

@admin.register(SocialMedia)
class SocialMedia(admin.ModelAdmin):
    list_display = ['id', 'order','link','icon','updated_date','created_date']
    search_fields = ['link']
    list_editable = ['link','icon']
    class Meta:
        model =SocialMedia