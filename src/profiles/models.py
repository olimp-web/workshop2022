from django.db import models


# Create your models here.
class ProfilePage(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название страницы")
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "профиль участника"
        verbose_name_plural = "профили участников"
