from django import template
register = template.Library()
@register.filter
#separates list of words (with a seperator in between) into separate strings 
def explode(value, separator):
    return value.split(separator)