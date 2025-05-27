from django import template

register = template.Library()

@register.filter
def multiply(x, y):
    return x * y