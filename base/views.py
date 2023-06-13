from django.shortcuts import get_object_or_404,render
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Project,StuffLink, ContactLink, InfoText, ProfileInfo,Experience
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    stufflinks = StuffLink.objects.all()
    contactlinks = ContactLink.objects.all()

    profile = ProfileInfo.objects.first()

    infotext = InfoText.objects.first()

    template_name = "base/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = self.profile.name
        context['bio'] = self.profile.bio
        context['info'] = self.infotext
        context["stufflinks"] = self.stufflinks
        context["contactlinks"] = self.contactlinks
        
        return context

class ProjectView(TemplateView):

    qs = Project.objects.all()

    template_name = "base/projects.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["projects"] = self.qs
        
        
        return context

class ExperienceView(TemplateView):

    qs = Experience.objects.all()

    template_name = "base/experiences.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["experiences"] = self.qs
        
        
        return context