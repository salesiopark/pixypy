from jinja2 import Template

"""
pixipy에서도 사용되므로 밖으로 빼논다.
"""
def render(file_name, **kwargs):
    file = open('pixipy/tmpl/'+file_name, 'r', encoding='utf8')
    code = Template(file.read()).render(kwargs)
    file.close()
    return code

"""
base class for PixiJS objects
"""
class PixiObj:
    def __init__(self, js_file=None):
        self._js_file = js_file # /tmpl/ 에 위치한 js template파일
        self._event_handler = None
        self._inits = None #초기 (지정된) attr 값들을 저장한다.
        self._update_func = None

    # self.x 는 self.__dict__['x'] 와 같다. 아래 메서드는
    # self.__dict__['x']를 self['x']와 같게 만든다.(읽기만 가능)
    def __getitem__(self, key):
        return self.__dict__[key]
    
    """
    self._event_handler 는 객체를 첫 인자로 넘긴다.
    따라서 외부함수에서 (자기)객체의 속성을 접근할 수 있다.
    """
    def set_event_handler(self, func):
        self._event_handler = func

    def _handle_event(self):
        if self._event_handler != None:
            return self._event_handler(self)
        else:
            return None
    
    '''
    사용자가 update 함수를 등록할 수 있다.
    pixipy 에서는 update 요구 시 self._update()함수를 호출한다.
    외부함수에서도 (자기)객체의 속성을 접근할 수 있다.
    '''
    def set_update_func(self, func):
        self._update_func = func

    def _update(self):
        if self._update_func != None:
            self._update_func(self)
        
    # update 에 사용될 attr 키들을 self._inits 딕에 저장한다.
    def _store_inits(self, *args):
        self._inits = {k:self[k] for k in args}
        
    # 등록된 attr중 초기값에서 변한 것들만 뽑아서 반환한다. 
    def _get_changed_attrs(self):
        ret = {k:self[k] for k in self._inits if self[k]!=self._inits[k]}
        if ret: return ret # ret가 {}라면 None 이 반환

    def _render_js(self):
        kwargs = self._inits.copy() # 반드시 *복사*한 후
        kwargs['name'] = self._name # name 필드를 추가해야 한다
        self._rendered_js_code = render(self._js_file, **kwargs)