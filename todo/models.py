from django.db import models

# Create your models here.

class Color(models.Model):
    code = models.CharField(max_length=20, verbose_name='ColorCode')
    color_title = models.CharField(max_length=20, verbose_name='Title')

    def __str__(self):
        return self.color_title

class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Task')
    description = models.TextField(verbose_name='Description')
    date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')
    is_done = models.BooleanField(default=False, verbose_name='Done')
    color = models.ForeignKey(Color,null=True, on_delete=models.CASCADE, verbose_name='Color')

    class Meta:
        verbose_name='Task'
        verbose_name_plural='Tasks'

    def __str__(self):
        return self.title



