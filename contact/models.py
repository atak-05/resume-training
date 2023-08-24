from django.db import models
from core.models import AbstractModel
# Create your models here.
class Message(AbstractModel):
    name= models.CharField(max_length=254,default="",blank=True,verbose_name="Name")
    email= models.EmailField(max_length=254,default="",blank=True,verbose_name="Email")
    subject= models.CharField(max_length=254,default="",blank=True,verbose_name="Subject")
    message= models.TextField(default="",blank=True,verbose_name="Message")

    def __str__(self):
        return f"Message {self.name} is sending to {self.email} about {self.subject} "

    class Meta:
         verbose_name="Message"
         verbose_name_plural="Messages"
         ordering = ('name',)