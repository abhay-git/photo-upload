from django.contrib import admin
from .models import *
# Register your models here.


class DocumentAdmin(admin.ModelAdmin):
	 list_display = ['title','docfile']


admin.site.register(Document,DocumentAdmin)