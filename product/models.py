from django.db import models

from autoslug import AutoSlugField
# Create your models here.

class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    
    parents = models.ForeignKey('self',blank=True, null=True, related_name='chilren', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    images = models.ImageField(upload_to ='images/',blank=True)
    status = models.CharField(max_length=50, choices=STATUS)
    slug = AutoSlugField(populate_from='title')
    # stock = models.IntegerField()
    # is_available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    # update_date = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #many to one relation with Category
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/')
    status = models.CharField(max_length=50, choices=STATUS)
    price = models.FloatField()
    amount=models.IntegerField()
    detail=models.TextField()
    stock = models.IntegerField()
    slug = AutoSlugField(populate_from='title')
    min_amount=models.IntegerField(default=3)
    is_available = models.BooleanField(default=True)
    create_date =models.DateTimeField(auto_now_add=True)
    update_date =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




    