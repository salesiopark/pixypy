from jinja2 import Template

def render(file_name, **kwargs):
    file = open('pixipy/tmpl/'+file_name, 'r', encoding='utf8')
    code = Template(file.read()).render(kwargs)
    file.close()
    return code

class PixiObj:
    def __init__(self):
        self._event_handler = None
    
    def _handle_event(self):
        if self._event_handler != None:
            return self._event_handler(self)
        else:
            return None
    
    def set_event_handler(self, func):
        self._event_handler = func

from .pixipy import Pixipy
from .text import Text
from .button import Button