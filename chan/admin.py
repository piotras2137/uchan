from django.contrib import admin
from .models import Thread, Respone, Board

admin.site.register(Board)
admin.site.register(Thread)
admin.site.register(Respone)