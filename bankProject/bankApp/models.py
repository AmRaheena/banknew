from django.db import models
from django.urls import reverse


# Create your models here.
class Branch(models.Model):
    br_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    District=models.CharField(max_length=250)
    IFSC_code=models.CharField(max_length=100)

    class Meta:
        ordering=('br_name',)
        verbose_name='branch'
        verbose_name_plural='branches'
    def get_url(self):
        return reverse('bankApp:Branches',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.br_name)

class Sub_branch(models.Model):
    br_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    IFSC_code=models.CharField(max_length=250)

    def get_url(self):
        return reverse('bankApp:sub_branches', args=[self.branch.slug, self.slug])

    class Meta:
        ordering = ('br_name',)
        verbose_name = 'sub_branch'
        verbose_name_plural = 'sub_branches'
    def __str__(self):
        return '{}'.format(self.br_name)





