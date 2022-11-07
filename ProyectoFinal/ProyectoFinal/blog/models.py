

from ast import Delete
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

class UserProfile(models.Model):
    nombre = models.CharField(max_length=300)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.nombre


     
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    cuerpo = models.TextField()
    header_image=models.ImageField(null=True,blank=True, upload_to="images/")
    publicado = models.DateTimeField(auto_now_add=True)
    presentar = models.BooleanField(blank = True, null = False, default=True)
    autor = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    
    
    def __str__(self):
        return self.titulo
   
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)
    
    
    
 


