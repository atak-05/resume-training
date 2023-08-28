from django import forms
from django.core.mail import EmailMessage

from resume1 import settings


class ContactForm(forms.Form):
    name = forms.CharField(max_length=254)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=254)
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        if self.is_valid():
            name= self.cleaned_data['name']
            email= self.cleaned_data['email']
            subject= self.cleaned_data['subject']
            message= self.cleaned_data['message']
            message_context= "Message received \n\n"\
                "Name: %s\n"\
                "Subject: %s\n"\
                "Email: %s\n"\
                "Message: %s" % (name, email,subject,message)

            email1= EmailMessage(subject=subject,body=message_context,to=[settings.DEFAULT_FROM_EMAIL],reply_to=[email])
            email1.send()