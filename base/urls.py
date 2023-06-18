from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "base"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("projects", views.ProjectView.as_view(), name="projects"),
    path("experience", views.ExperienceView.as_view(), name="experience"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)