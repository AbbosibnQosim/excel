from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=512)
    def __str__(self):
      return self.name
    class Meta:
        verbose_name_plural = 'Давлатлар'
        verbose_name = 'Давлат'


class ObjectType(models.Model):
    name=models.CharField(max_length=512)
    def __str__(self):
      return self.name
    class Meta:
        verbose_name_plural = 'Объект турлари'
        verbose_name = 'Объект тури'
class ResourceType(models.Model):
    name=models.CharField(max_length=512)
    def __str__(self):
      return self.name
    class Meta:
        verbose_name_plural = 'Ресурс турлари'
        verbose_name = 'Ресурс тури'



class Object(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    country=models.ForeignKey(Country,on_delete=models.CASCADE,verbose_name="Давлат")
    code=models.CharField(max_length=512,verbose_name="Код",blank=True)
    obtype=models.ForeignKey(ObjectType,on_delete=models.CASCADE,verbose_name="Объект тури")
    name=models.TextField(blank=False,verbose_name="Объект номи")
    address=models.TextField(blank=True,verbose_name="Манзил")
    coordination=models.CharField(max_length=256,verbose_name="Кордината",blank=True)
    phone=models.TextField(blank=True,verbose_name="Телефон")
    mails=models.TextField(blank=True,verbose_name="почталар")
    #websites=models.TextField(blank=True)
    subdomains=models.TextField(blank=True,verbose_name="Суб-доменлари")
    info_sys=models.TextField(blank=True,verbose_name="Ахборот тизимлари")
    ips=models.TextField(blank=True,verbose_name="IP адреслар")
    verified=models.BooleanField(default=False,verbose_name="Текширилган")
    description=models.TextField(blank=True,verbose_name="Тавсиф")
    content = RichTextUploadingField(blank=True,verbose_name="Ресултат")
    resultfile = models.FileField(verbose_name="Ресултат файл",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.name
    class Meta:
        verbose_name_plural = 'Объектлар'
        verbose_name = 'Объект'

class Website(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    url=models.CharField(max_length=2048)
    object=models.ForeignKey(Object,on_delete=models.CASCADE)
    rtype=models.ForeignKey(ResourceType,on_delete=models.CASCADE,verbose_name='Ресурс тури')
    ip=models.CharField(blank=True,max_length=16,verbose_name='IP адрес')
    server_cor=models.CharField(max_length=128,blank=True,verbose_name='Сервер координатаси')
    subdomains=models.TextField(blank=True,verbose_name='Суб доменлар')
    dirs=models.TextField(blank=True,verbose_name='Директориялар')
    tech=models.TextField(blank=True,verbose_name='Технология')
    open_ports=models.TextField(blank=True,verbose_name='Очиқ портлар')
    vulnerabilities=models.TextField(blank=True,verbose_name='Заифликлари')
    #domain=models.CharField(max_length=2048)
    
    
    verified=models.BooleanField(default=False,verbose_name="Текширилган")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
      return self.url
    class Meta:
        verbose_name_plural = 'Ресурслар'
        verbose_name = 'Ресурс'
    

class Result(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  website=models.ForeignKey(Website,on_delete=models.CASCADE,verbose_name="Сайт")
  positive=models.BooleanField(default=False,verbose_name="Natija")
  description=RichTextUploadingField(blank=True,verbose_name="Ресултат")
  resultfile = models.FileField(verbose_name="Ресултат файл",blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
      return self.website.url
  class Meta:
        verbose_name_plural = 'Ресултатлар'
        verbose_name = 'Ресултат'
  # @property
  # def html_stripped(self):
  #      from django.utils.safestring import mark_safe
  #      return mark_safe(self.description)


from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=Object)
def object_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.resultfile.delete(False)
@receiver(pre_delete, sender=Result)
def object_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.resultfile.delete(False)



    