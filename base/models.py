from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.project_name


class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="projects")
    project_link = models.CharField(max_length=200)
    link_text = models.CharField(max_length=200)
    def __str__(self):
        return self.project_link
        
class StuffLink(models.Model):
    thing_link = models.CharField(max_length=200)
    thing_text = models.CharField(max_length=200)
    def __str__(self):
        return self.thing_link
        
class ContactLink(models.Model):
    contact_link = models.CharField(max_length=200)
    contact_text = models.CharField(max_length=200)
    def __str__(self):
        return self.contact_link

class InfoText(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text

class ProfileInfo(models.Model):
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Experience(models.Model):
    exptype = models.CharField(max_length=200,choices=[("Full-Time","Full-Time"),("Part-Time","Part-Time"),("Volunteer","Volunteer")])
    title = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()
    def showStartTime(self):
        return  self.startdate.strftime("%B %Y")
    def showEndTime(self):
        return  self.enddate.strftime("%B %Y")
    def __str__(self):
        return self.title

    