from django.contrib import admin

from .models import *


admin.site.register(Profile)
admin.site.register(McqProblems)
admin.site.register(McqSubmissions)
admin.site.register(Contests)
admin.site.register(Event)

