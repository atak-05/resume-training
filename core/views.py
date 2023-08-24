from django.shortcuts import render, redirect,get_object_or_404
from core.models import GeneralSetting, ImageSettings, Skill, Experience, Education, SocialMedia, Document

def layout(request):
    documents= Document.objects.all()
    site_title = GeneralSetting.objects.get(name="site_title").parameters
    site_keywords = GeneralSetting.objects.get(name="site_keywords").parameters
    site_description = GeneralSetting.objects.get(name="site_description").parameters
    home_banner_name = GeneralSetting.objects.get(name="home_banner_name").parameters
    home_banner_title = GeneralSetting.objects.get(name="home_banner_title").parameters
    home_banner_description = GeneralSetting.objects.get(name="home_banner_description").parameters
    about_myself_welcome = GeneralSetting.objects.get(name="about_myself_welcome").parameters
    about_myself_footer = GeneralSetting.objects.get(name="about_myself_footer").parameters
    # Images
    header_logo = ImageSettings.objects.get(name="header_logo").file
    home_banner_image = ImageSettings.objects.get(name="home_banner_image").file
    site_favicon = ImageSettings.objects.get(name="site_favicon").file
    # Social Media
    social_media = SocialMedia.objects.all().order_by('order')

    documents = Document.objects.all()
    context = {
        'documents': documents,
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_welcome': about_myself_welcome,
        'about_myself_footer': about_myself_footer,
        'header_logo': header_logo,
        'home_banner_image': home_banner_image,
        'site_favicon': site_favicon,
        'social_media': social_media,
        'documents': documents,

    }
    return context
# Create your views here.
def index(request):

    #Skills
    skills =Skill.objects.all().order_by('order')

    #Experience
    experiences =Experience.objects.all().order_by('-start_date')

    #Education
    educations =Education.objects.all().order_by('-start_date')



    context = {

        'skills':skills,
        'experiences':experiences,
        'educations':educations,


    }
    return render(request, "index.html", context=context)

def redirect_urls(request,slug):
    doc=get_object_or_404(Document,slug=slug)
    if doc :
        return  redirect(doc.file.url)
    else:
        return redirect('index')