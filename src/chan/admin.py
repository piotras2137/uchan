from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Reply)
admin.site.register(News)
admin.site.register(FaqQuestion)
admin.site.register(Rule)
admin.site.register(SiteSettings)
