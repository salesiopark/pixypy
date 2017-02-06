import pixipy
import math

pp = pixipy.Pixipy(update=True)

#t1 = pixipy.Text()
t2 = pixipy.Text('hello pixipy', x=50)

b1 = pixipy.Button(y=100)
b2 = pixipy.Button(text="LED ON", x=100, y=200, width=100, height=40, font_size=15)

def isr(this):
    print(this._name+" clicked.")
    
b2.set_event_handler(isr)

pp.add(t2)
pp.add(b1)
pp.add(b2)
#pp.add(t2)
#

def upd(this):
    this.x += 0.1
    
b1.set_update_func(upd)
t2.set_update_func(upd)
    
pp.run()
#pp.run()