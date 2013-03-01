import logging
from django.template import Library

from banners.models import BANNER_WIDGETS, BannerBlock

logger = logging.getLogger(__name__)

register = Library()

@register.inclusion_tag('banners/list.html', takes_context=True)
def show_banners(context, block_title):
    target = context.get('content_obj')

    if target is None:
        return

    try:
        block = BannerBlock.objects.get(title=block_title)
    except BannerBlock.DoesNotExist:
        return

    logger.debug('try to show banners for block %s and target %s ' % (block, target))
    banners = target.get_banners().filter(banner_place=block)

    logger.debug('founded banners %s' % banners)

    return {'banners': banners,
            'block': block
           }
