from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(MenuItem)
admin.site.register(Cart)

