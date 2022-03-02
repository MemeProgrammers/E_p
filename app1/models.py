from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from pkg_resources import to_filename
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.


class Course(Model):
    title = models.CharField(help_text="Course name", max_length = 200)
    duration = models.BigIntegerField(help_text='Coure Duration')
    description = models.TextField(help_text='Course Description')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True,null=True,blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('course',kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.title

class Topic(Model):
    title = models.CharField(help_text='Topic Name', max_length = 200)
    description = models.TextField(help_text='Topic Description')
    duration = models.CharField(help_text = 'Topic Duration', max_length = 100)
    video = models.FileField(help_text='video/')
    article = models.TextField(help_text='Topic Article')
    likes = models.IntegerField(default=0)
    course = models.ForeignKey(Course, null=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('topic',kwargs={'slug':self.slug})
    
    def get_article_url(self):
        return reverse('article',kwargs={'slug':self.slug})
    
    def get_video_url(self):
        return reverse('video',kwargs={'slug':self.slug})
    
    def get_quiz_url(self):
        return reverse('quiz',kwargs={'slug':self.slug})
    
    def get_discussion_url(self):
        return reverse('discussion',kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.title
    
    
class Quiz(Model):
    question = models.CharField(help_text='Question', max_length = 200)
    answer = models.CharField(help_text='Answer', max_length = 200)
    option1 = models.CharField(help_text='option 1', max_length = 200)
    option2 = models.CharField(help_text='option 2', max_length = 200)
    option3 = models.CharField(help_text='option 3', max_length = 200)
    option4 = models.CharField(help_text='option 4', max_length = 200)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    
    
    
    
class QuizMarks(Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    date_attempted = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    score = models.IntegerField(default=0)
    


class Discussion(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(help_text='tell you opinion')
    topic = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE)
    
   
    
    
class Reply(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, null=True, on_delete=models.CASCADE)
    text = models.TextField(help_text='Reply for discussion')

