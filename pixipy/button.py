from .pixiobj import PixiObj

class Button(PixiObj):
    __cnt = 0
    
    def __init__(self, text=None, x=0, y=0, width=100, height=50, font_size=25):
        super().__init__('button.js')
        
        self._name = "button%d"%Button.__cnt
        if text == None: text = self._name
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        
        
        Button.__cnt += 1
        
        # 갱신 가능한 초기값들을 저장
        self._store_inits('x', 'y', 'text', 'width', 'height', 'font_size')
        #print(self._inits)
        
        '''
        self._code = self._render(name=self._name,
            text=text,
            x=x,
            y=y,
            width = width,
            height = height,
            font_size = font_size,
        )
        '''
        self._render_js()
