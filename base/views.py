from .models import Project, ProjectCategory, StuffLink, ContactLink, InfoText, ProfileInfo, Experience, ExperienceCategory,SourceLink
from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    stufflinks = StuffLink.objects.all()

    contactlinks = ContactLink.objects.all()

    profile = ProfileInfo.objects.first()

    infotext = InfoText.objects.first()

    sourcecode = SourceLink.objects.first()

    template_name = "base/index.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context['image'] = self.profile.image
        context['name'] = self.profile.name
        context['bio'] = self.profile.bio
        context['info'] = self.infotext
        context["stufflinks"] = self.stufflinks
        context["contactlinks"] = self.contactlinks
        context["sourcelink"] = self.sourcecode
        
        return context

class ProjectView(TemplateView):

    categories = ProjectCategory.objects.all().order_by("sort_id")
    projectdict = {}

    for i in categories:
        projectdict[i] = Project.objects.filter(projecttype=i).order_by("sort_id")

    sourcecode = SourceLink.objects.first()

    template_name = "base/projects.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["projectdictionary"] = self.projectdict
        context["sourcelink"] = self.sourcecode
        
        return context

class ExperienceView(TemplateView):

    categories = ExperienceCategory.objects.all().order_by("sort_id")
    expdict = {}

    for i in categories:
        expdict[i] = Experience.objects.filter(exptype=i).order_by("-startdate")

    sourcecode = SourceLink.objects.first()

    template_name = "base/experiences.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context ["expdictionary"] = self.expdict
        context["sourcelink"] = self.sourcecode
        
        return context