from math import ceil, cos, sin
from math import floor
import pygame;
import Paths;

class controls(object):
    def __init__(self,forward,backward,Left,Right):
        self.forward = forward
        self.backward = backward
        self.left = Left
        self.right = Right

Clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((480,360))
run = True
textures = []
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "1.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "2.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "3.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "4.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "5.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "6.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "7.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "8.png")))
textures.append(pygame.surfarray.array3d(pygame.image.load(Paths.textures + "9.png")))

texturewidth = 32
textureheight = 32

class player(object):
    def __init__(self,movespeed,x,y,rotspeed,Pcontrols):
        #Player Setup
        self.x = x
        self.y = y
        self.movespeed = movespeed
        self.rotspeed = rotspeed
        self.yaw = 0
        self.dirx = -1
        self.diry = 0
        self.plx = 0
        self.ply = 0.66
        self.controls = Pcontrols
    def plrupdate(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls.forward]:
            self.x += self.dirx * self.movespeed
            self.y += self.diry * self.movespeed
        if keys[self.controls.backward]:
            self.x -= self.dirx * self.movespeed
            self.y -= self.diry * self.movespeed
        if keys[self.controls.right]:
            self.olddirx = self.dirx
            self.dirx = self.dirx * cos(-self.rotspeed) - self.diry * sin(-self.rotspeed)
            self.diry = self.olddirx * sin(-self.rotspeed) + self.diry * cos(-self.rotspeed)
            self.oldplx = self.plx
            self.plx = self.plx * cos(-self.rotspeed) - self.ply * sin(-self.rotspeed)
            self.ply = self.oldplx * sin(-self.rotspeed) + self.ply * cos(-self.rotspeed)
        if keys[self.controls.left]:
            self.olddirx = self.dirx
            self.dirx = self.dirx * cos(self.rotspeed) - self.diry * sin(self.rotspeed)
            self.diry = self.olddirx * sin(self.rotspeed) + self.diry * cos(self.rotspeed)
            self.oldplx = self.plx
            self.plx = self.plx * cos(self.rotspeed) - self.ply * sin(self.rotspeed)
            self.ply = self.oldplx * sin(self.rotspeed) + self.ply * cos(self.rotspeed)


map = [
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,2,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,3,0,0,0,3,0,0,0,1],
  [1,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,2,2,0,2,2,0,0,0,0,3,0,3,0,3,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,5,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

print(textures[0][15][0])
#logic
plr = [player(0.125,3,3,0.05,controls(pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d)),player(0.125,3,3,0.05,controls(pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT))]

def raycast(playr,scrx,scry,width,height,renderquality):
    for x in range(floor(width / renderquality)):
        camerax = 2 * x / (floor(width / renderquality)) - 1
        raydirx = playr.dirx + playr.plx * camerax
        raydiry = playr.diry + playr.ply * camerax
        
        #Get Player Position
        mapx = floor(playr.x)
        mapy = floor(playr.y)

        #setup side dists
        sidedistx = 0
        sidedisty = 0

        #get ray length
        if raydirx == 0:
            deltadistx = 1e30
        else:
            deltadistx = abs(1 / raydirx)
        #get the other ray
        if raydiry == 0:
            deltadisty = 1e30
        else:
            deltadisty = abs(1 / raydiry)
        #cool

        # other variables

        stepx = 0
        stepy = 0

        hit = 0
        side = 0

        if raydirx < 0:
            stepx = -1
            sidedistx = (playr.x - mapx) * deltadistx
        else:
            stepx = 1
            sidedistx = ((mapx + 1) - playr.x) * deltadistx

        if raydiry < 0:
            stepy = -1
            sidedisty = (playr.y - mapy) * deltadisty
        else:
            stepy = 1
            sidedisty = ((mapy + 1) - playr.y) * deltadisty

        while hit == 0:
            if sidedistx < sidedisty:
                sidedistx += deltadistx
                mapx += stepx
                side = 1
            else:
                sidedisty += deltadisty
                mapy += stepy
                side = 0
            hit = map[mapx][mapy]
        texturenum = hit - 1
        wallx = 0
        if side == 0:
            perpwalldist = sidedisty - deltadisty
            texturequality = floor(perpwalldist / 8) + 1
            if perpwalldist > 0:
                lineheight = floor(height / perpwalldist)
            else:
                lineheight = height
            wallx = playr.x + perpwalldist * raydirx
            wallx -= floor(playr.x + perpwalldist * raydirx)
            wallcoord = floor(wallx * texturewidth) % texturewidth
            lineY = lineheight/2
            linedesty = lineY - (lineheight/textureheight)
            for y in range(ceil(textureheight / texturequality)):
                wally = y - 1
                if wally > floor(textureheight / texturequality):
                    wally = floor(textureheight / texturequality)
                for w in range(renderquality):
                    pygame.draw.line(win,(textures[texturenum][wallcoord][wally * texturequality][0] * 0.8, textures[texturenum][wallcoord][wally * texturequality][1] * 0.8, textures[texturenum][wallcoord][wally * texturequality][2] * 0.8),pygame.Vector2((x * renderquality) + w + scrx,(height / 2) + (lineY) + scry),pygame.Vector2((x * renderquality) + w + scrx,(height / 2) + (linedesty) + scry))
                lineY -= lineheight/textureheight * texturequality
                linedesty = lineY - (lineheight/textureheight) * texturequality
        else:
            perpwalldist = sidedistx - deltadistx
            texturequality = floor(perpwalldist / 8) + 1
            if perpwalldist > 0:
                lineheight = floor(height / perpwalldist)
            else:
                lineheight = height
            wallx = playr.y + perpwalldist * raydiry
            wallx -= floor(playr.y + perpwalldist * raydiry)
            wallcoord = floor(wallx * texturewidth) % texturewidth
            lineY = lineheight/2
            linedesty = lineY - (lineheight/textureheight)
            for y in range(ceil(textureheight / texturequality)):
                wally = y - 1
                if wally > floor(textureheight / texturequality):
                    wally = floor(textureheight / texturequality)
                for w in range(renderquality):
                    pygame.draw.line(win,(textures[texturenum][wallcoord][wally * texturequality][0], textures[texturenum][wallcoord][wally * texturequality][1], textures[texturenum][wallcoord][wally * texturequality][2]),pygame.Vector2((x * renderquality) + w + scrx,(height / 2) + (lineY) + scry),pygame.Vector2((x * renderquality) + w + scrx,(height / 2) + (linedesty) + scry))
                lineY -= lineheight/textureheight * texturequality
                linedesty = lineY - (lineheight/textureheight) * texturequality

def Gameupdate():
    plr[0].plrupdate()
    plr[1].plrupdate()
    win.fill((0,0,0))
    raycast(plr[0],0,0,240,360,4)
    raycast(plr[1],240,0,240,360,4)



while run:
    Clock.tick(60)
    Gameupdate()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
