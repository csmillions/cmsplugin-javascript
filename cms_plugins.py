from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Script

class JavasciptPlugin(CMSPluginBase):
    model = Script
    name = _('script')
    render_template = 'cmsplugin_javascript/script.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.__unicode__,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(JavasciptPlugin)