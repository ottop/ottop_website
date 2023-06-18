from django.contrib import admin

from .models import Project, ProjectLink, StuffLink, ContactLink, InfoText, ProfileInfo, Experience


admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(StuffLink)
admin.site.register(ContactLink)
admin.site.register(InfoText)
admin.site.register(ProfileInfo)
admin.site.register(Experience)