from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE #deletes stories whenn author is deleted
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    img_url = models.URLField(max_length = 250, default="https://picsum.photos/600")

    class Meta:
        ordering = ['pub_date'] #ordering by date