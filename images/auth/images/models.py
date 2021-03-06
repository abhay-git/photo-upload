from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

# Create your models here.
class Image(models.Model):
        title = models.CharField(max_length=200)
        slug = models.SlugField(max_length=200,blank=True)
        url = models.URLField()
        image = models.ImageField(upload_to='images/%Y/%m/%d')
        description = models.TextField(blank=True)
        created = models.DateField(auto_now_add=True,db_index=True)

        def __str__(self):
        	return self.title

        def save(self,*args,**kwargs):
        	if not self.slug:
        		self.slug = slugify(self.title)
        		super(Image,self).save(*args,**kwargs)

        def get_absolute_url():
        	return self.url


class Document(models.Model):
	    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	    #title = models.CharField(max_length=100,blank=True)