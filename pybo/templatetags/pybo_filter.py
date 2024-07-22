import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions)) # markdown.markdown() 함수를 이용하여 value를 HTML로 변환한 후 mark_safe() 함수를 이용하여 HTML을 브라우저에 출력할 수 있도록 변환한다.