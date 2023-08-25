from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
# Create your models here.



class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.caption}"



class Author(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    img = models.CharField(max_length=45)
    date = models.DateField(auto_now=True)
    slug= models.SlugField(unique=True,db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tag = models.ManyToManyField(Tag)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)


        super().save(*args,**kwargs) 