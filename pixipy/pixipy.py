from . import render

class Pixipy:
    
    def __init__(self, width=200, height=300):
        #self.__tmpl = self.__Template(open('pixipy/tmpl/index.html').read())
        self._width = width
        self._height = height
        self.__objs = []
        
    def run(self, func_upd=None, **kwargs):
        from flask import Flask
        from flask_cors import CORS, cross_origin
        from flask import jsonify
        #from flask import render_template
        #from flask import request

        app = Flask(__name__)
        CORS(app)

        js_objs = open('pixipy/tmpl/header.js','r',encoding='utf8').read()
        for obj in self.__objs :
            js_objs += obj._code
        
        self.html = render('index.html',
            width=self._width,
            height=self._height,
            objs=js_objs)
        
        print(self.html)
        
        @app.route('/')
        def index():
            return self.html

        @app.route('/update')
        def _upd():
            if func_upd != None: func_upd()
            objs = {}
            for obj in self.__objs:
                objs[obj._name] = obj.get_obj()
            return jsonify(objs)
        
        app.run()
        #print(self.html)
        
    def add(self, obj):
        self.__objs.append(obj)