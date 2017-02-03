from jinja2 import Template

def render(file_name, **kwargs):
    file = open('pixipy/tmpl/'+file_name, 'r', encoding='utf8')
    code = Template(file.read()).render(kwargs)
    file.close()
    return code


from .pixipy import Pixipy
from .text import Text
from .button import Button