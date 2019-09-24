from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save

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
    name_employee = models.CharField(max_length=100, verbose_name='Employee Name')
    name_job = models.CharField(max_length=100, verbose_name='Job Name')
    certificate = models.CharField(max_length=100, verbose_name='Certificate')
    mobile_number = models.CharField(max_length=10, verbose_name='Mobile Number')
    description = models.TextField(verbose_name='Description')
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
    body = models.TextField(verbose_name='Order details')
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-comment_date', )

def create_profile(sender, **kwarg):
    if kwarg['created']:
        user_profile = Post.objects.create(user=kwarg['instance'])

post_save.connect(create_profile, sender=User)