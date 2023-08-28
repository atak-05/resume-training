from django.shortcuts import render, redirect
from django.http import JsonResponse

from contact.forms import ContactForm
from contact.models import Message


# Create your views here.
def contact_form(request):
    if request.POST:
        contact_form1 = ContactForm(request.POST or None)
        if contact_form1.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            Message.objects.create(name=name, email=email, subject=subject, message=message)
            contact_form1.send_email()
            success = True
            message1 = 'Contact form sent successfully'

        else:
            success = False
            message1 = 'Contact form is not valid'

    else:
        success = False
        message1 = 'Request method is not valid'

    context = {'success': success,
               'message1': message1}

    print(message1)

    return JsonResponse(context)


def contact(request):
    contact_form1 = ContactForm()

    context = {
        'contact_form1': contact_form1,

    }
    return render(request, "contact.html", context=context)
