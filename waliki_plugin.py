from django.utils.translation import ugettext_lazy as _
from waliki.plugins import BasePlugin, register


class BlocksPlugin(BasePlugin):

    slug = 'blocks'
    urls_page = ['waliki_blocks.urls']
    extra_page_actions = {}
    navbar_links = ()
#    extra_page_actions = {'all': [('waliki_history', _('History'))]}
#    navbar_links = (('waliki_whatchanged', _('What changed')),)

register(BlocksPlugin)
