from django.db import models

class ProjectCategory(models.Model):
    category = models.CharField(max_length=200)
    sort_id = models.CharField(max_length=3)
    def __str__(self):
        return self.category

class Project(models.Model):
    projecttype = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE,related_name="projecttypes",blank=True,null=True)
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    sort_id = models.CharField(max_length=3)
    def __str__(self):
        return self.project_name

class ProjectLink(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="projects",blank=True,null=True)
    project_link = models.CharField(max_length=200)
    link_text = models.CharField(max_length=200)
    def __str__(self):
        return (self.link_text + " - " + self.project.project_name)
        
class StuffLink(models.Model):
    thing_link = models.CharField(max_length=200)
    thing_text = models.CharField(max_length=200)
    def __str__(self):
        return self.thing_text
        
class ContactLink(models.Model):
    contact_link = models.CharField(max_length=200)
    contact_text = models.CharField(max_length=200)
    def __str__(self):
        return self.contact_text

class InfoText(models.Model):
    text = models.TextField()
    def __str__(self):
        return self.text

class ProfileInfo(models.Model):
    
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    image = models.ImageField(null = True,blank=True,upload_to = "images")
    def __str__(self):
        return self.name

class ExperienceCategory(models.Model):
    category = models.CharField(max_length=200)
    sort_id = models.CharField(max_length=3)
    def __str__(self):
        return self.category

class Experience(models.Model):
    exptype = models.ForeignKey(ExperienceCategory, on_delete=models.CASCADE,related_name="experiencetypes",blank=True,null=True)
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField()
    def showStartTime(self):
        return  self.startdate.strftime("%B %Y")
    def showEndTime(self):
        return  self.enddate.strftime("%B %Y")
    def __str__(self):
        return (self.title + " - " + self.company)

class SourceLink(models.Model):
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.link