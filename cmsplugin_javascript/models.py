from django.utils.translation import ugettext as _
from django.db import models

from cms.models import CMSPlugin

class Script(CMSPlugin):
    content = models.TextField(_('script'))

    def __unicode__(self):
        return u'%s' % (self.content,)