from django.db import models
from .tools.slugify import slugify

# Create your models here.

# Меню
class Menu(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Элементы меню
class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, null=False, default='')
    title = models.CharField(max_length=50, null=False, unique=True)
    slug = models.SlugField(max_length=100, null=False, default='', editable=False)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    def generate_slug(self):
        slugs = [self.name]
        parent = self.parent
        while parent:
            slugs.append(parent.name)
            parent = parent.parent
        slugs.reverse()
        slugs.insert(0, 'materials')
        slugs.insert(0, slugify(self.menu.__str__()))
        return '/'.join(slugify(slug) for slug in slugs)

    def save(self, *args, **kwargs):
        self.slug = '/' + self.generate_slug()
        super().save(*args, **kwargs)
    
    def has_children(self):
        return self.children.exists()
    
    def has_parent(self):
        return True if self.parent else False
