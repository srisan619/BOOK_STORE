from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    # rating = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    rating = models.IntegerField()
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True)
        
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"slug": self.slug})
    
    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} {self.title} ({self.rating}) {self.is_bestselling} {self.author} {self.slug}"