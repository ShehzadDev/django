from django import template

register = template.Library()


@register.simple_tag
def greet(name):
    return f"Hello, {name}!"
