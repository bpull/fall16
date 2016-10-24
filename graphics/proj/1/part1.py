# pyglet event handler demo

import pyglet
from pyglet.window import mouse, key
from pyglet.gl import glEnable, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND
import imp

import sys
sys.dont_write_bytecode = True

# Our World
class Scene:
    # Move objects between keyboard input
    def movement(self, dt):
        print('%f seconds since last callback' %dt)

    # Initialize and run our environment
    def __init__(self, width=800, height=600, caption="Would you like to play a game?"):

        self.levelname = sys.argv[-1]
        self.level = imp.load_source('happy',self.levelname+'.py')

        # Build the OpenGL / Pyglet Window
        self.window = pyglet.window.Window(width=width, height=height, caption=caption)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self.keys = key.KeyStateHandler()

        # Create the Background
        self.background = pyglet.resource.image(self.level.background)
        self.background_x = 0

        self.sound = pyglet.media.load(self.level.music)

        self.keys_pressed = {'jump':False, 'left':False, 'right':False, 'attack':False, 'throw':False, 'sprint':False}

        # Schedule player movements
        pyglet.clock.schedule_interval(self.movement, 10)

        self.window.push_handlers(self.keys)

        # Event Handler for drawing the screen
        @self.window.event
        def on_draw():
            self.window.clear()
            self.background.blit(self.background_x,0,height=height)
            self.level.drawBoard(self.level.level)
            self.level.drawBoard(self.level.goals)

        @self.window.event
        def on_key_press(symbol, modifiers):
            if symbol == key.SPACE or symbol == key.UP:
                self.keys_pressed['jump'] = True
            if symbol == key.LEFT:
                self.keys_pressed['left'] = True
            if symbol == key.RIGHT:
                self.keys_pressed['right'] = True
            if symbol == key.LALT or symbol == key.RALT:
                self.keys_pressed['attack'] = True
            if symbol == key.LCTRL or symbol == key.RCTRL:
                self.keys_pressed['throw'] = True
            if symbol == key.LSHIFT or symbol == key.RSHIFT:
                self.keys_pressed['sprint'] = True
            print (self.keys_pressed)


        @self.window.event
        def on_key_release(symbol, modifiers):
            if symbol == key.SPACE or symbol == key.UP:
                self.keys_pressed['jump'] = False
            if symbol == key.LEFT:
                self.keys_pressed['left'] = False
            if symbol == key.RIGHT:
                self.keys_pressed['right'] = False
            if symbol == key.LALT or symbol == key.RALT:
                self.keys_pressed['attack'] = False
            if symbol == key.LCTRL or symbol == key.RCTRL:
                self.keys_pressed['throw'] = False
            if symbol == key.LSHIFT or symbol == key.RSHIFT:
                self.keys_pressed['sprint'] = False
            print (self.keys_pressed)


if __name__ == '__main__':
    myGame = Scene()
    pyglet.app.run()
