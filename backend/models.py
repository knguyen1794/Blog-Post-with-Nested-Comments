from django.db import models

# Create your models here.

class Post(models.Model):
    post = models.TextField()
    
class Comment(models.Model):
    comment = models.CharField(max_length=250)
    from_post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='from_post')
    parent = models.ForeignKey('self', related_name='reply_set', null=True, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
