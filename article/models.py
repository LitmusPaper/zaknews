from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
User = settings.AUTH_USER_MODEL
import os
import random
from django.utils.text import slugify

def upload_to(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return '%s/user_%s/%s%s'%('article',instance.author.id,random.randrange(100,999),file_extension)

class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Taq')
    slug = models.SlugField(max_length=100, unique=True,blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name = 'Taq'
        verbose_name_plural = 'Taqlar'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Article(models.Model):
    author = models.ForeignKey(User, verbose_name = 'Müəllif',related_name='article', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Başlıq', blank=False, null=False)
    content = RichTextField(max_length=5000, verbose_name='Yazı', blank=False, null=False)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarix')
    image = models.ImageField(blank=True, null=True, verbose_name='Başlıq Şəkli', upload_to=upload_to)
    tags = models.ManyToManyField(Tag, verbose_name='Taqlar')
    slug = models.SlugField(max_length=250, editable=False)

    class Meta:
        verbose_name = 'Məqalə'
        verbose_name_plural = 'Məqalələr'
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return '%  %' % (self.title,self.author)
    
    def get_img_or_default(self):
        if self.image and hasattr(self.image,'url'):
            return self.image.url
        return '/media/img/default.jpg'



class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE, verbose_name='Yazan')
    article = models.ForeignKey(Article, related_name='comments',on_delete=models.CASCADE, verbose_name='Məqalə')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Tarix')
    content = models.TextField(max_length=500,verbose_name='Şərh')

    class Meta:
        verbose_name = 'Şərh'
        verbose_name_plural = "Şərhlər"
        ordering = ('-created_date',)


    def __str__(self):
        return '{} > {}'.format(self.author,self.article)
    
    def __unicode__(self):
        return '{} > {}'.format(self.author,self.article)

