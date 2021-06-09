from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Market, self).save(*args, **kwargs)
    
    def get_experts(self):
        return self.experts.all()
