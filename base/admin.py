from django.contrib import admin

from .models import Project, ProjectLink,ProjectCategory, StuffLink, ContactLink, InfoText, ProfileInfo, Experience, ExperienceCategory,SourceLink


admin.site.register(Project)
admin.site.register(ProjectLink)
admin.site.register(ProjectCategory)
admin.site.register(StuffLink)
admin.site.register(ContactLink)
admin.site.register(InfoText)
admin.site.register(ProfileInfo)
admin.site.register(Experience)
admin.site.register(ExperienceCategory)
admin.site.register(SourceLink)