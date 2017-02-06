import pixipy
import math

pp = pixipy.Pixipy()

t1 = pixipy.Text(x=50, y=100)
t2 = pixipy.Text('hello pixipy', x=100, y=200, font_size=50)

pp.add(t1)
pp.add(t2)

t1._cnt = 0
def upd1(this):
    this.font_size = 30+20*math.sin(t1._cnt/20)
    this.text = str(this._cnt)
    this.y += 0.1
    this._cnt += 1

t1.set_update_func(upd1)    

pp.run()