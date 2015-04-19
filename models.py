import os
from django.db.models import Max
from random import randint
from django.template import Library, Template, Context
from django.template.loader import get_template
from django.db import models
from django.conf import settings
from waliki.models import Page
from zutils.models import SuperModel, RandomModel, DisplayModel, ZUtilModel


#import os, pkgutils
#def get_packages():
#  plugin_paths = settings.BLOCKS_PLUGINS if hasattr(settings, 'BLOCKS_PLUGINS') else []
#
#  mod_path = os.path.abspath(__file__)
#  dir_path = os.path.sep.join( (os.path.dirname(mod_path), 'plugins'), )
#  plugin_paths.insert(0, dir_path)
#
#for package in get_packages():
#  for i, m, p in pkgutils.iter_modules(package, ''):
# http://stackoverflow.com/questions/1707709/list-all-the-modules-that-are-part-of-a-python-package

#def static_vars(**kwargs):
#    def decorate(func):
#        for k in kwargs:
#            setattr(func, k, kwargs[k])
#        return func
#    return decorate

class Block(ZUtilModel):
  name = models.CharField(max_length=40, blank=True)
  page = models.ForeignKey(Page)

  def __unicode__(self): return self.title

  @property
  def title(self): return self.actual.get_title()
  def get_title(self): return self.name

class InfoBox(Block):
  image = models.ImageField(upload_to='blocks/images', blank=True, null=True)
  caption = models.CharField(max_length=60, blank=True, null=True)

  class Meta:
    verbose_name = 'infobox'
    verbose_name_plural = 'infoboxes'

class InfoBoxSection(models.Model):
  name = models.CharField(max_length=60)
  infobox = models.ForeignKey(InfoBox)

  class Meta:
    verbose_name = 'section'
    verbose_name_plural = 'sections'

class InfoBoxEntry(models.Model):
  label = models.CharField(max_length=60)
  text = models.CharField(max_length=100)
  link = models.URLField(blank=True, null=True)
  section = models.ForeignKey(InfoBoxSection)

  class Meta:
    verbose_name = 'entry'
    verbose_name_plural = 'entries'

class QuipBox(Block):
  def random_quip(self):
    return Quip.random.filter(quipbox=self).random()

class Quip(RandomModel):
  quip = models.CharField(max_length=500)
  quipbox = models.ForeignKey('QuipBox')

