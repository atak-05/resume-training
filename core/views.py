from django.shortcuts import render
from core.models import GeneralSetting, ImageSettings, Skill


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name="site_title").parameters
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameters
    site_description = GeneralSetting.objects.get(name="site_description").parameters
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameters
    home_banner_title = GeneralSetting.objects.get(name="home_banner_title").parameters
    home_banner_description =GeneralSetting.objects.get(name="home_banner_description").parameters
    about_myself_welcome =GeneralSetting.objects.get(name="about_myself_welcome").parameters
    about_myself_footer =GeneralSetting.objects.get(name="about_myself_footer").parameters
    #Images
    header_logo =ImageSettings.objects.get(name="header_logo").file
    home_banner_image =ImageSettings.objects.get(name="home_banner_image").file
    site_favicon =ImageSettings.objects.get(name="site_favicon").file
    #Skills
    skills =Skill.objects.all().order_by('order')
    context = {
        'site_title': site_title,
        'site_keywords':site_keywords,
        'site_description':site_description,
        'home_banner_name':home_banner_name,
        'home_banner_title':home_banner_title,
        'home_banner_description':home_banner_description,
        'about_myself_welcome':about_myself_welcome,
        'about_myself_footer':about_myself_footer,
        'header_logo':header_logo,
        'home_banner_image':home_banner_image,
        'site_favicon':site_favicon,
        'skills':skills,
    }
    return render(request, "index.html", context=context)

