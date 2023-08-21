from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class AbstractModel(models.Model):
    updated_date = models.DateField(auto_now_add=True, blank=True, verbose_name='updated date', help_text='')
    created_date = models.DateField(auto_now=True, blank=True, verbose_name='created date', help_text='')

    class Meta:
        abstract = True

class GeneralSetting(AbstractModel):
    name = models.CharField(max_length=254, default='', verbose_name='name', help_text='this is variable of settings')
    description = models.CharField(max_length=254, default='', blank=True, verbose_name='description', help_text='')
    parameters = models.CharField(max_length=254, default='', blank=True, verbose_name='parameters', help_text='')


    def __str__(self):
        return f"General Setting: {self.name}"

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"
        ordering = ("name",)


class ImageSettings(AbstractModel):
    name = models.CharField(default='', max_length=254,blank=True, verbose_name='Name', help_text='This is variable of setting.')
    description=models.CharField(default='', max_length=254,blank=True, verbose_name='Description', help_text='')
    file=models.ImageField(default='', blank=True, verbose_name='Image', help_text='',upload_to='images/')


    def __str__(self):
        return f"Image Setting: {self.name}"

    class Meta:
        verbose_name = "Image Setting"
        verbose_name_plural = "Image Settings"
        ordering = ("name",)

class Skill(AbstractModel):
    order = models.IntegerField(default=0,verbose_name="Order")
    name = models.CharField(default='', max_length=254,blank=True, verbose_name='Name', help_text='This is variable of setting.')
    percentage = models.IntegerField(default=50, verbose_name="Percent",validators=[MinValueValidator(0),MaxValueValidator(100)])

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ("order",)