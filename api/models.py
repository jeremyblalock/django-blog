from django.db import models
from django.contrib.auth.models import User
import markdown
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    body_md = models.TextField(blank=False)
    body = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, blank=True, null=True)
    slug = models.CharField(max_length=255, unique=True)
    likes = models.IntegerField(default=0)
    def save(self, *args, **kwargs):
        self.body = markdown.markdown(self.body_md)
        if not self.slug:
            count = 1
            self.slug = slugify(self.title)
            while True:
                try:
                    self.save()
                    break
                except:
                    self.slug = slugify(self.title)
                    count += 1
        return super(self.__class__, self).save(*args, **kwargs)
    def update_likes(self):
        likes = len(Like.object.filter(post=self))
        self.likes = likes
        self.save()

class Like(models.Model):
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    def save(self):
        self.post.update_likes()
        self.post.save()
        return super(Likes, self).save()

