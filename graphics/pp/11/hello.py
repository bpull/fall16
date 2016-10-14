import pyglet
from pyglet.window import key, mouse

window = pyglet.window.Window()
window.push_handlers(pyglet.window.event.WindowEventLogger())
music = pyglet.resource.media('nacho.mp3')
music.play()

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print ("A")
    elif symbol == key.LEFT:
        print ("Left arrow")
    elif symbol == key.ENTER:
        print ("enter key")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print ("left click at "+str(x)+","+str(y))

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
