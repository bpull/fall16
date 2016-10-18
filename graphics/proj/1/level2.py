# Game Level Configuration file!

# Note: if you have problems with transparent images, add the following
#   lines after your cleate the pyglet window!
#
#         # Fix transparent issue...
#         glEnable(GL_BLEND)
#         glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
#
#   And import this within that library!
#
#        # Load Graphics Libraries
#        import pyglet
#        from pyglet.gl import glEnable, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA, GL_BLEND

# Assuming a 800x600 world, allowed to go beyond in x and y,
# divided up into 50x50 chunks.

# Define the board
levelDefinition = '''
20
19
18
17
16
15                                                                hl hm hm hr
14
13                                                          hl hm hm hr
12
11                                                    hl hm hm hr
10
09                                        hl hm hm hr                         hl hm hm hr
08                                                                                                 hl hm hm hr
07                   hl hm hm hm hm hm hm hm hr
06
05          hl hr
04                                                                ul ur
03 um ur                                                       ul cl cr ur
02 mm mr                                                       ml mm mm mr             ul ur       ul ur
01 mm cr wl um um um um um um um um ur       ul um um um um um cl mm mm cr um um um um cl cr um um cl cr um um ur                ul
00 mm mm mm mm mm mm mm mm mm mm mm mr       ml mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm mm cr um um um um um cl
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
'''

# Define the objects
goalDefinition = '''
11
10
09
08
07
06
05
04
03
02
01                                                                                                                      sm
00
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
'''

# Define the enemies
enemyDefinition = '''
11
10
09
08                               e1    e2
07
06
05
04
03
02                                              e1                                           e1
01
00
00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43
'''

# Define where the player will start on the board
playerStartRow = 4
playerStartCol = 9

# Define where the background image is
background = "background/level1.png"

# Define what music to play
music = 'music/1.wav'

# Sound Effects
heroSoundFire = 'music/throw.wav'
heroSoundAttack = 'music/attack.wav'
heroSoundWin = 'music/win.wav'
heroSoundJump = 'music/jump.wav'
heroSoundDeath = 'music/hero_death.wav'
enemySoundDeath = 'music/enemy_death.wav'

# Where are the tiles located?
tilepath = 'sprites/tiles'
goalpath = 'sprites/objects'

# Prevent the cleation of pyc files
import sys
sys.dont_write_bytecode = True

# Import the pyglet library
import pyglet

# A function to cleate a useful grid from the board file...
def board2grid(board, tilepath='sprites/tiles', returnSize=False):
    board = board.split('\n')[1:-2]
    board.reverse()
    results = {}
    resultsType = {}
    row = 0
    max_cols = 0
    for line in board:
        col = 0
        line = line[2:]
        while len(line) > 2:
            current = line[:3].strip()
            line = line[3:]
            if current != '':
                if not row in results:
                    results[row] = {}
                    resultsType[row] = {}
                try:
                    results[row][col] = pyglet.image.load(tilepath+"/"+current+".png")
                    resultsType[row][col] = current
                except:
                    print('Bad definition at row='+str(row) +', col='+str(col)+', image='+current+'.png')
            if col > max_cols:
                max_cols = col
            col += 1
        row += 1
    if returnSize:
        return results, row, max_cols
    return results

def drawBoard(level, delta_x=0, delta_y=0, height=50, width=50):
    for row in level.keys():
        for col in level[row].keys():
            level[row][col].anchor_x = 0
            level[row][col].anchor_y = 0
            level[row][col].blit(col*width+delta_x,row*height+delta_y, height=height, width=width)

def positionEnemies(board):
    board = board.split('\n')[1:-2]
    board.reverse()
    results = []
    row = 0
    max_cols = 0
    for line in board:
        col = 0
        line = line[2:]
        while len(line) > 2:
            current = line[:3].strip()
            line = line[3:]
            if current != '':
                results.append([col,row,current])
            if col > max_cols:
                max_cols = col
            col += 1
        row += 1
    return results

# cleate the useful grid for drawing later...
enemies = positionEnemies(enemyDefinition)
level, rows, cols = board2grid(levelDefinition, tilepath, returnSize=True)
goals = board2grid(goalDefinition, goalpath)
