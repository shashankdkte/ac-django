from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Author(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)

   def fullname(self):
      return f"{self.first_name}   {self.last_name} "
   
   def __str__(self):
      return self.fullname()


class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField(
    validators=[MinValueValidator(1),MaxValueValidator(5)]
  )
  author = models.ForeignKey(Author, on_delete=models.CASCADE,null = True)
  is_bestselling = models.BooleanField(default=False)
  slug = models.SlugField(default="",blank = True,null=False,db_index=True)


  def __str__(self):
    return f" Books info : \n\t title:{self.title} \n\t rating:  {self.rating}\n\t author: {self.author} \n\t bestSeller: {self.is_bestselling}\n\n"
  
  def get_absolute_url(self):
      return reverse("book-detail", args=[self.slug])
  
  def save(self,*args, **kwargs):
     self.slug = slugify(self.title)
     super().save( *args, **kwargs)