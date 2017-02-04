from . import render
from . import PixiObj

class Text(PixiObj):
    __cnt = 0
    
    def __init__(self, text=None, x=0, y=0, font_size=15):
        super().__init__()
        self._name = "text%d"%Text.__cnt
        if text == None: text = self._name
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size
        
        self._code = render('text.js',
            name = self._name,
            text = text,
            x = x,
            y = y,
            font_size = font_size
        )
        
        Text.__cnt += 1

        #갱신 가능한 초기값들을 저장
        self._store_inits('x', 'y', 'text', 'font_size')
        #print(self._inits)