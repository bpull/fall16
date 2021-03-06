#Brandon Pullig 175148
#SI460 2017

import pyglet
from pyglet.window import mouse, key
from pyglet.gl import glEnable, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND
import imp
import time
import math
import sys

sys.dont_write_bytecode = True

#Our players
class Player:
    def __init__(self, startRow, startCol, images, sounds, typePlay):
        #x and y hold pixel value of location
        self.x = (startCol+1)*50
        self.y = (startRow-2)*50

        self.dir = "right"

        #specifies what type of player (ie hero, enemy)
        self.typePlayer = typePlay
        self.power = 0
        self.speed = 3

        #setting respective power levels
        if self.typePlayer == "hero":
            self.power = 1
        elif self.typePlayer == "e1":
            self.speed = 4
            self.power = 2
        elif self.typePlayer == "e2":
            self.speed = 2
            self.power = 2
        elif self.typePlayer == "weapon":
            self.speed = 5
            self.power = 3

        #images hold all the sprites necessary for this object
        self.imgs = images
        self.sounds = sounds

        #start the animated list
        self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["idle"], 0.05, True)
        if self.typePlayer == "e1" or self.typePlayer == "e2":
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
        self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
        self.sprite.scale = 0.15

        #modifiers that affect the player and his current options
        self.fast = False
        self.idle = True
        self.att = False
        self.jumping = False
        self.running = False
        self.time = 0
        self.steps = 0
        self.stepJump = 31
        self.lastDelta = 0
        self.fallingSpeed = 1.0
        self.collisionGround = True
        self.collisionWall = False
        self.about2Fall = False
        self.died = False
        self.won = False
        self.checked = False

  #controls the left and right movement
    def motion(self):
        if self.dir == "right":
            if self.fast:
                self.x += 9
            else:
                self.x += self.speed
        else:
            if self.fast:
                self.x -= 9
            else:
                self.x -= self.speed

        self.sprite.x = self.x
        self.sprite.scale = .15

    #controls the sword swing
    def attack(self):
        #if not currently attacking...
        if not self.att:
            self.sounds["attack"].play()
            self.time = time.time()
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["attack"], 0.05, False)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.power = 3
            self.att = True

   #animation for throwing weapon
    def throw(self):
        if not self.att:
            self.sounds["fire"].play()
            self.time = time.time()
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["throw"], 0.05, False)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.att = True

    #splits the jump into 2 halves; first 15 is going up and the next 15 is the start downwards
    def jump(self):
        if self.stepJump < 16:
            self.lastDelta = math.sin(math.radians(self.stepJump*90.0/15.0))*160 - math.sin(math.radians((self.stepJump-1)*90.0/15.0))*160
            self.y += self.lastDelta
        elif self.stepJump < 30:
            if self.fallingSpeed < 45:
                self.fallingSpeed *= 1.1
            else:
                self.fallingSpeed = 45
            self.y -= self.fallingSpeed
        else:
            self.jumping = False
            if self.running:
                self.steps = 10
                self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
                if self.dir == "left":
                    self.startAnim = self.startAnim.get_transform(flip_x=True)
                self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y-2)

        self.stepJump += 1
        self.sprite.y = self.y
        self.sprite.scale = .15

    #how to act when no input is entered
    def idleAct(self):
        if self.att and time.time() > self.time+0.5:
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["idle"], 0.05, True)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.idle = True
            self.att = False
        if self.idle == False:
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["idle"], 0.05, True)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.idle = True

    #this checks the vertical collisions with the ground as well as the horizontal collisions with walls and edges
    def checkCollision(self,level,cols):
        row = int(math.floor((self.sprite.y) / 50))
        col = int(math.floor(self.sprite.x / 50))
        # print row
        # print col

        #check if falling
        if row not in level or col not in level[row]:
            self.collisionGround = False
            if self.fallingSpeed < 45:
                self.fallingSpeed *= 1.1
            else:
                self.fallingSpeed = 45
            self.sprite.y -= self.fallingSpeed
            self.y = self.sprite.y
        #otherwise, we are on the ground
        else:
            self.collisionGround = True
            self.fallingSpeed = 1.0
            self.sprite.y = (row+1)*50-1
            self.y = self.sprite.y

        #this is the death pit check
        if row <= -1:
            self.died = True
            self.fallingSpeed = 0
            self.sprite.y = (row+1)*50
            self.y = self.sprite.y

        #this is checking horizontal collisions with walls
        if row+1 in level and col+1 in level[row+1] and self.dir == "right":
            self.collisionWall = True
            if self.fast:
                self.x -= 9
            else:
                self.x -= 3

        elif row+1 in level and col-1 in level[row+1] and self.dir == "left":
            self.collisionWall = True
            if self.fast:
                self.x += 9
            else:
                self.x += 3

        else:
            self.collisionWall = False

        #checking if the ground spot infront of you is empty (ie are you about to fall off the edge)
        if self.collisionGround and ((self.dir == "right" and col+1 not in level[row]) or (self.dir == "left" and col-1 not in level[row])):
            self.about2Fall = True
        else:
            self.about2Fall = False

        #checking if next to the boundary
        if col == 0:
            self.x = 50
        elif col == cols+2:
            self.x = cols*50

    #the constant walking for zombies
    def creep(self, level, cols):
        self.idle = False
        self.running = True
        self.checkCollision(level, cols)
        if self.collisionWall or self.about2Fall:
            if self.dir is "left":
                self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
                self.dir = "right"
                self.x -= 35
                self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
                self.sprite.scale = 0.15

            else:
                self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
                self.dir = "left"
                self.startAnim = self.startAnim.get_transform(flip_x=True)
                self.x += 35
                self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
                self.sprite.scale = 0.15

        self.motion()

    #this will check if the character is dead; if so, play the animation and music once each
    def checkDead(self):
        if self.died and not self.checked:
            self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["dead"], 0.05, False)
            if self.dir == "left":
                self.startAnim = self.startAnim.get_transform(flip_x=True)
            self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
            self.sprite.scale = 0.15
            self.sounds["death"].play()
            self.checked = True

    #this checks if our current location is the same as the snowman
    def checkWin(self, goal):
        row = int(math.floor((self.sprite.y) / 50))+1
        col = int(math.floor(self.sprite.x / 50))

        if row in goal and col in goal[row]:
            self.sounds["win"].play()
            self.won = True

    #the meat of the player class. It is the controller for all other method definitions.
    #it takes in the actions (or keys pressed dictionary) and determines what move should
    #be next to act
    def action(self,actions,level,cols,goal):
        self.checkCollision(level,cols)
        self.checkDead()
        if not self.died and not self.won:
            self.checkWin(goal)
            if actions["sprint"]:
                self.fast=True
            else:
                self.fast=False
            if actions["attack"]:
                self.attack()
            elif actions["throw"]:
                self.throw()
            if actions["jump"] or self.stepJump < 31:
                if self.jumping == False:
                    self.sounds["jump"].play()
                    self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["jump"], 0.05, False)
                    if self.dir == "left":
                        self.startAnim = self.startAnim.get_transform(flip_x=True)
                    self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
                    self.stepJump = 1
                    self.lastDelta = 0
                    self.jumping = True
                    self.idle = False
                    self.fallingSpeed = .909
                self.jump()
            if actions["left"]:
                if (self.idle or self.dir == "right"):
                    self.steps = 10
                    self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
                    self.dir = "left"
                    self.startAnim = self.startAnim.get_transform(flip_x=True)
                    self.x += 25
                    self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
                    self.idle = False
                    self.running = True
                self.motion()
            elif actions["right"]:
                if (self.idle or self.dir == "left"):
                    self.steps = 10
                    self.startAnim = pyglet.image.Animation.from_image_sequence(self.imgs["run"], 0.05, True)
                    self.dir = "right"
                    self.x -= 25
                    self.sprite = pyglet.sprite.Sprite(self.startAnim, x=self.x, y=self.y)
                    self.idle = False
                    self.running = True
                self.motion()
            elif self.steps > 0:
                self.steps -= 1
                self.motion()
            else:
                self.running = False
            if not self.jumping and not self.running:
                self.idleAct()

# Our World
class Scene:
    # Move objects between keyboard input
    def movement(self, dt):
        self.hero.action(self.keys_pressed,self.level.level,self.level.cols, self.level.goals)
        for badguy in self.badguys:
            badguy.creep(self.level.level, self.level.cols)

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

        #Background music
        self.music = pyglet.media.load(self.level.music)
        self.music.play()

        #dictionary of hero sounds
        self.heroSounds = {"fire":pyglet.media.load(self.level.heroSoundFire, streaming=False)}
        self.heroSounds.update({"win":pyglet.media.load(self.level.heroSoundWin, streaming=False)})
        self.heroSounds.update({"jump":pyglet.media.load(self.level.heroSoundJump, streaming=False)})
        self.heroSounds.update({"attack":pyglet.media.load(self.level.heroSoundAttack, streaming=False)})
        self.heroSounds.update({"death":pyglet.media.load(self.level.heroSoundDeath, streaming=False)})

        #dictionary of enemy sounds
        self.enemySounds = {"death":pyglet.media.load(self.level.enemySoundDeath, streaming=False)}

        #keys pressed dictionary
        self.keys_pressed = {'jump':False, 'left':False, 'right':False, 'attack':False, 'throw':False, 'sprint':False}

        #dictionary to hold all sprites
        self.SPRITES = {}

        #get hero pictures
        runImages = []
        jumpImages = []
        idleImages = []
        deadImages = []
        throwImages = []
        attackImages = []
        for i in range(10):
            runImages.append(pyglet.image.load("sprites/hero/Run ("+str(i+1)+").png"))
            jumpImages.append(pyglet.image.load("sprites/hero/Jump ("+str(i+1)+").png"))
            idleImages.append(pyglet.image.load("sprites/hero/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/hero/Dead ("+str(i+1)+").png"))
            throwImages.append(pyglet.image.load("sprites/hero/Throw ("+str(i+1)+").png"))
            attackImages.append(pyglet.image.load("sprites/hero/Attack ("+str(i+1)+").png"))

        self.SPRITES.update({"hero":{"run":runImages, "jump":jumpImages, "idle":idleImages, "dead":deadImages, "throw":throwImages, "attack":attackImages}})

        #get enemy pictures
        runImages = []
        idleImages = []
        deadImages = []
        attackImages = []
        for i in range(8):
            runImages.append(pyglet.image.load("sprites/enemy-1/Run ("+str(i+1)+").png"))
            idleImages.append(pyglet.image.load("sprites/enemy-1/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-1/Dead ("+str(i+1)+").png"))
            attackImages.append(pyglet.image.load("sprites/enemy-1/Attack ("+str(i+1)+").png"))
        for i in range(8,10):
            runImages.append(pyglet.image.load("sprites/enemy-1/Run ("+str(i+1)+").png"))
            idleImages.append(pyglet.image.load("sprites/enemy-1/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-1/Dead ("+str(i+1)+").png"))
        for i in range(10,12):
            idleImages.append(pyglet.image.load("sprites/enemy-1/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-1/Dead ("+str(i+1)+").png"))
        for i in range(12,15):
            idleImages.append(pyglet.image.load("sprites/enemy-1/Idle ("+str(i+1)+").png"))

        self.SPRITES.update({"e1":{"run":runImages, "idle":idleImages, "dead":deadImages, "attack":attackImages}})

        #get enemy-2 pictures
        runImages = []
        idleImages = []
        deadImages = []
        attackImages = []
        for i in range(8):
            runImages.append(pyglet.image.load("sprites/enemy-2/Run ("+str(i+1)+").png"))
            idleImages.append(pyglet.image.load("sprites/enemy-2/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-2/Dead ("+str(i+1)+").png"))
            attackImages.append(pyglet.image.load("sprites/enemy-2/Attack ("+str(i+1)+").png"))
        for i in range(8,10):
            runImages.append(pyglet.image.load("sprites/enemy-2/Run ("+str(i+1)+").png"))
            idleImages.append(pyglet.image.load("sprites/enemy-2/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-2/Dead ("+str(i+1)+").png"))
        for i in range(10,12):
            idleImages.append(pyglet.image.load("sprites/enemy-2/Idle ("+str(i+1)+").png"))
            deadImages.append(pyglet.image.load("sprites/enemy-2/Dead ("+str(i+1)+").png"))
        for i in range(12,15):
            idleImages.append(pyglet.image.load("sprites/enemy-2/Idle ("+str(i+1)+").png"))

        self.SPRITES.update({"e2":{"run":runImages, "idle":idleImages, "dead":deadImages, "attack":attackImages}})

        #get knife images
        runImages = []
        for i in range(10):
            runImages.append(pyglet.image.load("sprites/weapon/Kunai ("+str(i+1)+").png"))

        self.SPRITES.update({"weapon":{"move":runImages}})

        #create the hero and all of the bad guys
        self.hero = Player(self.level.playerStartRow, self.level.playerStartCol, self.SPRITES["hero"], self.heroSounds, "hero")
        self.badguys = []
        for badguy in self.level.enemies:
            self.badguys.append(Player(badguy[0], badguy[1], self.SPRITES[badguy[2]], self.enemySounds, badguy[2]))


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
            for badguy in self.badguys:
                badguy.sprite.draw()

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
