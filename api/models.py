from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.title

    def number_of_likes(self):
        likes = Like.objects.filter(post=self)
        return len(likes)


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=False, blank=False
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False
    )
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = (("user", "post"),)
        index_together = (("user", "post"),)
