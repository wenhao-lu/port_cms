from django.contrib import admin
from .models import Project, Education, Work, Stack


# Register your models here.
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(Stack)
