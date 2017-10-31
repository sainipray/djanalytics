from django import template

register = template.Library()


@register.filter
def get_image(url):
    return url.replace("_normal", "")


@register.filter
def get_list(array, position):
    array = list(map(lambda x: x[int(position)], array))
    return array