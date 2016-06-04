from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    change_date = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=2000)
    def __unicode__(self):
        return u'%s: %s' % (self.author, self.text)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey('self', null=True, blank=True, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    def __unicode__(self):
        return u'%s: %s' % (self.author, self.text)

# Create your models here.
