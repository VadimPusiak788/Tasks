from django.db import models
from account.models import CustomUser
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='posts_image')
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Comment(models.Model):
    comments = models.CharField(max_length=256)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_comment = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comments} - {self.post_comment.title}'
