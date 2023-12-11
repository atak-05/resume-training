from django.shortcuts import render, redirect,get_object_or_404
from core.models import GeneralSetting, ImageSettings, Skill, Experience, Education, SocialMedia, Document

def get_general_setting(parameters):
    try:
        obj= GeneralSetting.objects.get(name=parameters).parameters
    except:
        obj=""

    return obj

def get_image_setting(parameters):
    try:
        obj= ImageSettings.objects.get(name=parameters).file
    except:
        obj=""
    return obj

def layout(request):
    site_title = get_general_setting('site_title')
    site_keywords = get_general_setting('site_keywords')
    site_description = get_general_setting('site_description')
    home_banner_name = get_general_setting('home_banner_name')
    home_banner_title = get_general_setting('home_banner_title')
    home_banner_description = get_general_setting('home_banner_description')
    about_myself_welcome = get_general_setting('about_myself_welcome')
    about_myself_footer = get_general_setting('about_myself_footer')



    # Images
    header_logo = get_image_setting('header_logo')
    home_banner_image = get_image_setting('home_banner_image')
    site_favicon = get_image_setting('site_favicon')
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
def about(request):

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

def home(request):

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
    return render(request, "home_1.html", context=context)