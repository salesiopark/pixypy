from .pixiobj import render

class Pixipy:
    
    def __init__(self,
                 width=200,
                 height=300,
                 background_color = 0x000000,
                 update=False,
                 update_time=100
                ):
        #self.__tmpl = self.__Template(open('pixipy/tmpl/index.html').read())
        self._width = width
        self._height = height
        self._background_color = background_color
        self.__objs = []
        
        # 만약 update_time 이 지정되었다면
        # js 에 setInterval() 함수 코드를 추가한다.
        self._js_update = ''
        if update:
            self._js_update += render('update.js', update_time=update_time)

        
    def run(self, func_upd=None, **kwargs):
        from flask import Flask
        from flask_cors import CORS, cross_origin
        from flask import jsonify
        from flask import request
        #from flask import render_template

        app = Flask(__name__)
        CORS(app)

        js_objs = open('pixipy/tmpl/header.js','r',encoding='utf8').read()
        for obj in self.__objs :
            js_objs += obj._rendered_js_code
        print(js_objs)
                    
        
        self.html = render('index.html',
            width = self._width,
            height = self._height,
            background_color = self._background_color,
            objs = js_objs,
            update = self._js_update)
        
        print(self.html)
        
        @app.route('/')
        def index():
            return self.html

        @app.route('/update')
        def _upd():
            if func_upd != None: func_upd()
            objs = {}
            for obj in self.__objs:
                obj._update()
                obj_attrs = obj._get_changed_attrs()
                if obj_attrs:
                    objs[obj._name] = obj_attrs
            return jsonify(objs)
        
        @app.route('/event')
        def _event():
            obj_name = request.args.get('obj', 0, type=str)
            ret = None
            for obj in self.__objs:
                if obj._name == obj_name:
                    ret = obj._handle_event()
                    
            return jsonify( {'ret':ret} )
        
        app.run()
        #print(self.html)
        
    def add(self, obj):
        self.__objs.append(obj)