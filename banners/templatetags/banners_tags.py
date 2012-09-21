from django.template import Library

from banners.models import BANNER_WIDGETS, BannerBlock

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

    banners = target.get_banners().filter(banner_place=block)

    return {'banners': banners,
            'block': block
           }
