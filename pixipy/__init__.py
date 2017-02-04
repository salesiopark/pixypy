from jinja2 import Template

def render(file_name, **kwargs):
    file = open('pixipy/tmpl/'+file_name, 'r', encoding='utf8')
    code = Template(file.read()).render(kwargs)
    file.close()
    return code

class PixiObj:
    def __init__(self):
        self._event_handler = None
        self._inits = None

    # self.x 는 self.__dict__['x'] 와 같다. 아래 메서드는
    # self.__dict__['x']를 self['x']와 같게 만든다.(읽기만 가능)
    def __getitem__(self, key):
        return self.__dict__[key]
    
    # self._event_handler 는 객체를 첫 인자로 넘긴다.
    # 따라서 외부함수에서 (자기)객체의 속성을 접근할 수 있다.
    def _handle_event(self):
        if self._event_handler != None:
            return self._event_handler(self)
        else:
            return None
    
    def set_event_handler(self, func):
        self._event_handler = func
        
    # update 에 사용될 attr 키들을 self._inits 딕에 저장한다.
    def _store_inits(self, *args):
        self._inits = {k:self[k] for k in args}

    # 등록된 attr중 초기값에서 변한 것들만 뽑아서 반환한다. 
    def _get_changed_attrs(self):
        ret = {k:self[k] for k in self._inits if self[k]!=self._inits[k]}
        if ret: return ret # ret가 {}라면 None 이 반환

from .pixipy import Pixipy
from .text import Text
from .button import Button