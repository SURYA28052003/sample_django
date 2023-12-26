from django.db import models

# Create your models here.
class Blog(models.Model):
    author_name = models.CharField(max_length = 200, editable=False , default = 'surya' )
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=5000)
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.title
