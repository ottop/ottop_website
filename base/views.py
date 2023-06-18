from .models import Project,StuffLink, ContactLink, InfoText, ProfileInfo, Experience
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    stufflinks = StuffLink.objects.all()

    contactlinks = ContactLink.objects.all()

    profile = ProfileInfo.objects.first()

    infotext = InfoText.objects.first()

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['image'] = self.profile.image
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

    qs = Experience.objects.all().order_by("-startdate")

    template_name = "base/experiences.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["experiences"] = self.qs
        
        return context