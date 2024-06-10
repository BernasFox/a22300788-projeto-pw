from django import template

register = template.Library()

@register.filter
def concat_str(value, arg):
    return str(value) + str(arg)
