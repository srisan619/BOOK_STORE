from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    street = models.CharField(max_length=100)

    def full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    def __str__(self):
        return self.full_address()
    
    class Meta:
        verbose_name_plural = "Address Entries"

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name="author", null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    # rating = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    rating = models.IntegerField()
    # author = models.CharField(null=True, max_length=100)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    # Harry Potter 1 => harry-potter-1
    slug = models.SlugField(default="", null=False, db_index=True)
    published_countries = models.ManyToManyField(Country, null=False, related_name="books")
        
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"slug": self.slug})
    
    # def save(self,*args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.id} {self.title} ({self.rating}) {self.is_bestselling} {self.author} {self.slug}"