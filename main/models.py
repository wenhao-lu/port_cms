from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)  
    url = models.URLField(null=True, blank=True) 
    github = models.URLField(null=True, blank=True) 
    image = models.ImageField(upload_to='projects/',null=True, blank=True)  
    subtitle = models.TextField(null=True, blank=True)  
    content1 = models.TextField(null=True, blank=True)  
    content2 = models.TextField(null=True, blank=True)  
    content3 = models.TextField(null=True, blank=True)  
    stacks = models.ManyToManyField('Stack', related_name='projects', blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Education(models.Model):
    degree = models.CharField(max_length=100)  
    major = models.CharField(max_length=50,null=True, blank=True)  
    school = models.CharField(max_length=50,null=True, blank=True)
    date = models.CharField(max_length=50,null=True, blank=True)
    course = models.CharField(max_length=255,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.degree


class Work(models.Model):
    title = models.CharField(max_length=100)  
    position = models.CharField(max_length=100,null=True, blank=True)  
    duration = models.CharField(max_length=100,null=True, blank=True)
    url = models.URLField(null=True, blank=True) 
    github = models.URLField(null=True, blank=True) 
    image = models.ImageField(upload_to='works/',null=True, blank=True)  
    subtitle = models.TextField(null=True, blank=True)  
    content1 = models.TextField(null=True, blank=True)  
    content2 = models.TextField(null=True, blank=True)  
    content3 = models.TextField(null=True, blank=True)  
    stacks = models.ManyToManyField('Stack', related_name='works', blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Stack(models.Model):
    name = models.CharField(max_length=100)  
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='stacks/',null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

