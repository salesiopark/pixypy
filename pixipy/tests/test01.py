import pixipy
import math

pp = pixipy.Pixipy()

t1 = pixipy.Text()
t2 = pixipy.Text('hello pixipy', x=50)

pp.add(t1)
pp.add(t2)

t1._cnt = 0
def upd():
    t1.font_size = 30+20*math.sin(t1._cnt/20)
    t1.text = str(t1._cnt)
    t1.y += 0.1
    t1._cnt += 1

pp.run(upd)