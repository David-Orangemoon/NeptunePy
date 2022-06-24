from math import cos, sin
from math import floor
import pygame;

Clock = pygame.time.Clock()
pygame.init()
win = pygame.display.set_mode((480,360))
run = True

class player(object):
    def __init__(self,movespeed,x,y,rotspeed):
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
    def plrupdate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += self.dirx * self.movespeed
            self.y += self.diry * self.movespeed
        if keys[pygame.K_s]:
            self.x -= self.dirx * self.movespeed
            self.y -= self.diry * self.movespeed
        if keys[pygame.K_d]:
            self.olddirx = self.dirx
            self.dirx = self.dirx * cos(-self.rotspeed) - self.diry * sin(-self.rotspeed)
            self.diry = self.olddirx * sin(-self.rotspeed) + self.diry * cos(-self.rotspeed)
            self.oldplx = self.plx
            self.plx = self.plx * cos(-self.rotspeed) - self.ply * sin(-self.rotspeed)
            self.ply = self.oldplx * sin(-self.rotspeed) + self.ply * cos(-self.rotspeed)
        if keys[pygame.K_a]:
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

#logic

plr = player(0.125,3,3,0.05)

def raycast(playr,scrx,scry,width,height):
    for x in range(width):
        camerax = 2 * x / width - 1
        raydirx = plr.dirx + plr.plx * camerax
        raydiry = plr.diry + plr.ply * camerax
        
        #Get Player Position
        mapx = floor(plr.x)
        mapy = floor(plr.y)

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
        
        if side == 0:
            perpwalldist = sidedisty - deltadisty
            if perpwalldist > 0:
                lineheight = floor(height / perpwalldist)
            else:
                lineheight = height
            pygame.draw.line(win,pygame.Color(0, 0, 150),pygame.Vector2(x,(height / 2) + (lineheight / 2)),pygame.Vector2(x,(height / 2) - (lineheight / 2)))
        else:
            perpwalldist = sidedistx - deltadistx
            if perpwalldist > 0:
                lineheight = floor(height / perpwalldist)
            else:
                lineheight = height
            pygame.draw.line(win,pygame.Color(0, 0, 250),pygame.Vector2(x,(height / 2) + (lineheight / 2)),pygame.Vector2(x,(height / 2) - (lineheight / 2)))

def Gameupdate():
    plr.plrupdate()
    win.fill((0,0,0))
    raycast(plr,0,0,480,360)



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