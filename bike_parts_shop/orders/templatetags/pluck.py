from django import template
register = template.Library()

@register.filter
def pluck(value, key):
    return [v.get(key) for v in value]
