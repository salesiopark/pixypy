#from . import render
#from . import PixiObj
from .pixiobj import PixiObj

class Text(PixiObj):
    __count = 0
    
    def __init__(self, text=None, x=0, y=0, font_size=30):
        super().__init__('text.js')
        
        self._name = "text%d"%Text.__count
        if text == None: text = self._name
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size

        #갱신 가능한 초기값들을 저장
        self._store_inits('x', 'y', 'text', 'font_size')
        self._render_js();
        
        Text.__count += 1