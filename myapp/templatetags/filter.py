from django.template.defaulttags import register
from django import template

register = template.Library()

@register.filter(name='truncate_to_10_words')
def truncate_to_10_words(value):
    words = value.split()[:4]
    truncated_text = ' '.join(words)
    truncated_text = truncated_text + '...'
    return truncated_text