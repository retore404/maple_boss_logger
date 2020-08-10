from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

@register.filter
def item(dictionary, key):
    return dictionary.get(key)