from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedTabularInline, NestedModelAdmin
from models import *

# this would look nicer tabular, but it's broken
class InfoBoxEntryAdmin(NestedStackedInline):
  model = InfoBoxEntry
  extra = 1
  fk_name = 'section'

class InfoBoxSectionAdmin(NestedStackedInline):
  model = InfoBoxSection
  extra = 1
  fk_name = 'infobox'
  inlines = [ InfoBoxEntryAdmin ]

class InfoBoxAdmin(NestedModelAdmin):
  fields = (('name', 'page'), ('image','caption'))
  inlines = [ InfoBoxSectionAdmin ]

admin.site.register(InfoBox, InfoBoxAdmin)

class QuipAdmin(models.StackedInline):
  fields = ('quips',)

class QuipBoxAdmin(models.Model):
  inlines = [ QuipAdmin, ]
