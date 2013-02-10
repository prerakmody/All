from django.db import models
from django.forms import ModelForm
from django import forms 
from datetime import date
from datetime import datetime

current_year = datetime.now().year
def tuplify(x):return (x,x)
YEARS = map(tuplify,range(1930, current_year + 1))

class user(models.Model):
    first_name = models.CharField(max_length=30,help_text="Enter your first name:")
    last_name = models.CharField(max_length=40)
    dob=models.DateField(default=date.today)
    batch=models.IntegerField(max_length=4,choices=YEARS)
    field=models.CharField(max_length=30)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='/tmp')
    added = models.DateTimeField(db_index=True, auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    def __uncode__(self):
        return u"%s %s" %(self.first_name,self.last_name)

class alumni(models.Model):
    basic=models.ForeignKey(user)
    city = models.CharField(max_length=60)
    website = models.URLField(null=True, blank=True)
    state = models.CharField(max_length=30)
    curr_employer=models.CharField(max_length=30)
    rollno=models.IntegerField(max_length=10)

    def __unicode__(self):
        return self.name

class mod_form_alumni(forms.ModelForm):
    #def __init__(self,*args,**kwargs):
        #self.fields['basic'].queryset = self.basic.objects.all()
    class Meta:
        model=alumni
        
        #fields=('basic.objects.all()','city',)
         #   to_field_name='basic')

        #fields=('name','dob','batch')
#class search_alumni(ModelForm):
 #   search=forms.CharField()
  #  class Meta:
   #     model=alumni
    #    fields('batch','field','city')



class faculty(models.Model):
    basic=models.ForeignKey(user)
    salutation = models.CharField(max_length=10)

class mod_form_faculty(ModelForm):
    class Meta:
        model=faculty
# Create your models here.



