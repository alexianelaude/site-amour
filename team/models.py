from django.db import models

# Create your models here.
def rename(instance, file_name):
    return "images/%s" % (instance.name)

def rename_gif(instance, file_name):
    return "gif/%s" % (instance.name)

class Listeux(models.Model):
    name = models.CharField(max_length = 200)
    poste = models.CharField(max_length = 500)
    description = models.TextField()
    image = models.ImageField(upload_to = rename, null = True)
    gif = models.ImageField(upload_to = rename_gif, null = True)
