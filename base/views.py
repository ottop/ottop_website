from django.shortcuts import get_object_or_404,render
from django.utils import timezone

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    infofile = open("base/static/base/infotext","r")
    infotext = infofile.read()
    infofile.close()

    template_name = "base/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Otto Petäjä"
        context['bio'] = "Developer"
        context['info'] = self.infotext
        context["ghlink"] = "https://github.com/ottop"
        context["itchlink"] = "https://ottop.itch.io/"
        context["gplink"] = "https://play.google.com/store/apps/developer?id=ottop"
        context["emailtext"] = "ottop.contact@gmail.com"
        context["emaillink"] = "mailto:ottop.contact@gmail.com"
        context["lilink"] = "https://www.linkedin.com/in/otto-petaja/"
        
        return context

class ProjectView(TemplateView):

    template_name = "base/projects.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['project1name'] = "Shell Jump Go"

        context['project1link1'] = "https://github.com/ottop/Shell_Jump_Go"
        context['project1link1name'] = "GitHub"

        context['project1link2'] = "https://ottop.itch.io/shell-jump-go"
        context['project1link2name'] = "Itch.io"

        context['project1link3'] = "https://play.google.com/store/apps/details?id=org.ottop.Shell_Jump_Go"
        context['project1link3name'] = "Google Play"
        
        return context
