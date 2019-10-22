from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinLengthValidator, int_list_validator

class Post(models.Model):
    image_logo = models.ImageField(default='default.jpg', upload_to='logo_co')
    image_post = models.ImageField(default='default.jpg', upload_to='post_co')
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-post_date', )

class Jobnew(models.Model):
    name_job = models.CharField(max_length=100, verbose_name='Job Name')
    description = models.TextField(verbose_name='Description')
    Job_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_job
    
    class Meta:
        ordering = ('-Job_date', )

class Jobrequest(models.Model):
    name_employee = models.CharField(max_length=100, verbose_name='Employee Name', default= None)
    name_job = models.CharField(max_length=100, verbose_name='Job Name', default= None)
    certificate = models.CharField(max_length=100, verbose_name='Certificate', default= None)
    mobile_number = models.IntegerField(blank=True, null=True, verbose_name='Mobile_number', default= None)
    uploaad_cv = models.FileField(upload_to='upload_cv', max_length=100, null=True, blank=True)
    description = models.TextField(verbose_name='Description', default= None)
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name_job
    
    class Meta:
        ordering = ('-post_date', )


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name='Company Name')
    email = models.EmailField(verbose_name='Email')
    nepersnt = models.CharField(max_length=50, verbose_name='Person Name', default= None)
    nopersnt = models.CharField(max_length=10, verbose_name='Person Number', default= None)
    body = models.TextField(verbose_name='Order Details')
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-comment_date', )

