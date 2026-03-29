from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)
    
    class Meta:    
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f"{self.cat_name}"
    
class Post(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    # featured_image = models.ImageField(upload_to="post-images/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=150, null=False, blank=False)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.title} - {self.author} on {self.created_at}"
    
