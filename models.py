from django.db import models
from django.conf import settings
from waliki.models import Page

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

class Block(models.Model):
  name = models.CharField(max_length=40, blank=True)
  page = models.ForeignKey(Page)

  @property
  def actual(self):
    if hasattr(self, '_actual'): return self._actual
    for name in [ model._meta.model_name for model in models.get_models() ]:
      try:
        self._actual = getattr(self, name)
        return self._actual
      except: pass
    return self

  @property
  def title(self): return self.actual.get_title()
  def get_title(self): return self.name

  @property
  def content(self):
    pass # need a request object here.. templatetag?

class InfoBox(Block):
  content = models.CharField(max_length=10)
