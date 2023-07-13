from django.db import models


class News(models.Model):
    image = models.ImageField(upload_to='news_images/',default='default_image.jpg')
    date = models.DateField()
    time = models.TimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    # def __str__(self):
    #     return self.title
