from typing import Any
from django.db import models
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify

# Create your models here.
class Tag(models.Model):
  caption = models.CharField(max_length=20)

  def __str__(self):
    return self.caption
  
class Author(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email_address = models.EmailField()

  def fullName(self):
    return f"{self.first_name}   {self.last_name}"
  
  def __str__(self) -> str:
    return self.fullName()

class Post(models.Model):  
  title = models.CharField(max_length=150)
  excerpt= models.CharField(max_length=200)
  image = models.ImageField(upload_to="posts", null=True)  
  image_name = models.CharField(max_length=100, null=True)
  date = models.DateField(auto_now=True)
  slug = models.SlugField(unique=True, db_index=True)
  content = models.TextField(validators=[MinLengthValidator(10)])
  author = models.ForeignKey(Author,on_delete=models.SET_NULL, related_name="posts",null=True)
  tags = models.ManyToManyField(Tag,null=False)

  def save(self,*args, **kwargs):
    self.slug = slugify(self.title)
    super().save( *args, **kwargs)

  def __setattr__(self, __name: str, __value: Any) -> None:
    return super().__setattr__(__name, __value)