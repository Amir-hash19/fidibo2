from django.db import models
from account.models import UserAccount
from django.utils.text import slugify



class Book(models.Model):
      
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
      
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(to=UserAccount, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    date_created = models.DateTimeField(auto_now_add=True)
    digital_version = models.FileField(upload_to="books/digital_versions/", null=True, blank=True, help_text="Upload the digital version (PDF, EPUB, etc.)")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    


    def __str__(self):
        return "{} - {}".format(self.title, self.status)




