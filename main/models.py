from distutils.command.upload import upload
from django.db import models
# Create your models here.

class Faculty(models.Model):
    title = models.CharField(verbose_name="Fakultet nomi", max_length=50)
    desc = models.TextField(verbose_name="Fakultet xaqida", blank=True)
    image = models.ImageField(verbose_name="Fakultet rasmi", upload_to="faculty_photo", blank=True)


class Category(models.Model):
    title = models.CharField(max_length=25)
    desc = models.TextField(verbose_name="Category xaqida", blank=True)
    image = models.ImageField(verbose_name="Category rasmi", upload_to="Category_photo", blank=True)
    def __str__(self):
        return self.title
    
    class Mete:
        verbose_name =  'Categorya'
        verbose_name_plural ='Categoryalar'

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    title = models.CharField(max_length=25)
    desc = models.TextField(verbose_name="kitob xaqida", blank=True)
    image = models.ImageField(verbose_name="kitob rasmi", upload_to="kitob_photo", blank=True)
    file =  models.FileField()
    def __str__(self):
        return self.title

    class Mete:
        verbose_name =  'kitob'
        verbose_name_plural ='kitoblar'


class Contact(models.Model):
    student = models.ForeignKey('reader.Student', on_delete = models.CASCADE,null=True)
    name = models.CharField(max_length=55,blank=True)
    email = models.EmailField(max_length=55,blank=True)
    subject = models.CharField(max_length=100)
    msg = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    showed = models.BooleanField(default=False)