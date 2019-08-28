import pyglet
from pyglet.gl import *
from math import pi, sin, cos, sqrt, asin, exp, log

WIDTH = 1024
HEIGHT = 768

window = pyglet.window.Window(width = WIDTH, height= HEIGHT)
window.set_fullscreen()
window.set_mouse_visible(False)

t = pos_x = pos_y = task = 0
r = 50


def circle(x, y, radius):
    """
    Source: https://sites.google.com/site/swinesmallpygletexamples/immediate-circle

    We want a pixel perfect circle. To get one,
    we have to approximate it densely with triangles.
    Each triangle thinner than a pixel is enough
    to do it. Sin and cosine are calculated once
    and then used repeatedly to rotate the vector.
    I dropped 10 iterations intentionally for fun.
    """

    iterations = int(2*radius*pi)
    s = sin(2*pi / iterations)
    c = cos(2*pi / iterations)

    dx, dy = radius, 0

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(iterations+1):
        glVertex2f(x+dx, y+dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    glEnd()

@window.event
def on_draw():
	global visible
	window.clear()
	if task == 0:
		circle(pos_x,pos_y,r)
		visible = 1

	if task == 1:
		if sin(t) > 0:
			circle(pos_x,pos_y,r)
			visible = 1
		else:
			visible = 0

	if task == 2:
		if (sin(t) > 0 and cos(t) > 0) or (sin(t) < 0 and cos(t) < 0):
			circle(pos_x,pos_y,r)
			visible = 1
		else:
			visible = 0



def record(dt):
	global t, pos_x, pos_y
	t += dt
	pos_x = sin(t)*200 + window.width/2 - r/2
	pos_y = cos(t)*200 + window.height/2 - r/2

    
@window.event
def on_key_press(symbol,modifiers):
	global task 
	## 48 en el teclado de mi portatil corresponde con el 0
	#print(symbol)
	key = symbol - 48

	if key == 1:
		task = 0
		print("Pursuit")

	if key == 2:
		task = 1
		print("Saccades_1")

	if key == 3:
		task = 2
		print("Saccades_2")

pyglet.clock.schedule(record)
pyglet.app.run()