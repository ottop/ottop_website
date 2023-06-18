from django.contrib import admin
from django.urls import include, path
from django_otp.admin import OTPAdminSite
from django.contrib.auth.models import User
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

from base.models import Project, ProjectLink, StuffLink, ContactLink, InfoText, ProfileInfo, Experience

class OTPAdmin(OTPAdminSite):
    pass

admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

admin_site.register(Project)
admin_site.register(ProjectLink)
admin_site.register(StuffLink)
admin_site.register(ContactLink)
admin_site.register(InfoText)
admin_site.register(ProfileInfo)
admin_site.register(Experience)

urlpatterns = [
    path('admin/', admin_site.urls),
    path("", include("base.urls")),
]
