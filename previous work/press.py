from time import sleep

from pykeyboard import PyKeyboard
from pymouse import PyMouse, PyMouseEvent


def gather(x):
    global x_dim, y_dim, m
    # for i in range(x):
    sleep(1)
    m.click(x_dim*2/3, y_dim/3, 2)
    # m.press(x_dim*2/3, y_dim/3, 2)
        # m.release(x_dim*2/3, y_dim/3, 2)

def moving():
    k = PyKeyboard()
    k.tap_key('w')

# class Clickonacci(PyMouseEvent):
  
#     def __init__(self):
#         PyMouseEvent.__init__(self)

#     def click(self, x, y, button, press):
#         # left click on somewhere for a few times after a right click
#         if button == 1:
#             if press:
#                 print press
#                 gather(2)
#         else: # Exit if any other mouse button used
#             self.stop()

def fibo():
    a = 0
    yield a 
    b = 1
    yield b 
    while True:
        a, b = b, a+b
        yield b 


m = PyMouse()
x_dim, y_dim = m.screen_size()
# m.release(x_dim*2/3, y_dim/3, button=2)
gather(3)
# c = Clickonacci()
# c.run()
