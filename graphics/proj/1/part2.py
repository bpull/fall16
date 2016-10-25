# pyglet event handler demo

import pyglet
from pyglet.window import mouse, key
from pyglet.gl import glEnable, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND
import imp

import sys
sys.dont_write_bytecode = True

#Our players
class Player:
    def __init__(self, startRow, startCol, typePlayer, images):
        self.x = (startCol+1)*50
        self.y = (startRow-2)*50
        self.playerName = typePlayer
        self.power = 0
        self.dir = "right"
        self.imgs = images
        self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["Idle"], 0.05, True)
        self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
        self.sprite.scale = 0.15
        self.fast = False
        self.idle = True


    def motion(self, direct):
        if self.idle == True:
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["Run"], 0.05, True)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.idle = False
        self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
        self.sprite.scale = .15

        if self.dir != direct:
            self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.dir = direct

        if self.dir == "right":
            if self.fast:
                self.x += 9
            else:
                self.x += 3
        else:
            if self.fast:
                self.x -= 9
            else:
                self.x -= 3



    def idleAct(self):
        if self.idle == False:
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["Idle"], 0.05, True)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.idle = True


    def action(self,actions):
        if actions["sprint"]:
            self.fast=True
        else:
            self.fast=False
        if actions["jump"]:
            self.jump()
        elif actions["left"]:
            self.motion("left")
        elif actions["right"]:
            self.motion("right")
        elif actions["attack"]:
            self.attack()
        elif actions["throw"]:
            self.throw()
        else:
            print("idle called")
            self.idleAct()

# Our World
class Scene:
    # Move objects between keyboard input
    def movement(self, dt):
        self.hero.action(self.keys_pressed)

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
        #self.sound.play()

        self.keys_pressed = {'jump':False, 'left':False, 'right':False, 'attack':False, 'throw':False, 'sprint':False}

        #get hero pictures
        runImagesHero = []
        jumpImagesHero = []
        idleImagesHero = []
        deadImagesHero = []
        throwImagesHero = []
        attackImagesHero = []
        for i in range(10):
            runImagesHero.append(pyglet.image.load("sprites/hero/Run ("+str(i+1)+").png"))
            jumpImagesHero.append(pyglet.image.load("sprites/hero/Jump ("+str(i+1)+").png"))
            idleImagesHero.append(pyglet.image.load("sprites/hero/Idle ("+str(i+1)+").png"))
            deadImagesHero.append(pyglet.image.load("sprites/hero/Dead ("+str(i+1)+").png"))
            throwImagesHero.append(pyglet.image.load("sprites/hero/Throw ("+str(i+1)+").png"))
            attackImagesHero.append(pyglet.image.load("sprites/hero/Attack ("+str(i+1)+").png"))

        images = {"Run":runImagesHero, "Jump":jumpImagesHero, "Idle":idleImagesHero, "Dead":deadImagesHero, "Throw":throwImagesHero, "Attack":attackImagesHero}

        self.hero = Player(self.level.playerStartRow, self.level.playerStartCol, "hero", images)

        # Schedule player movements
        pyglet.clock.schedule_interval(self.movement, .02)

        self.window.push_handlers(self.keys)

        # Event Handler for drawing the screen
        @self.window.event
        def on_draw():
            self.window.clear()
            self.background.blit(self.background_x,0,height=height)
            self.level.drawBoard(self.level.level)
            self.level.drawBoard(self.level.goals)
            self.hero.sprite.draw()

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
