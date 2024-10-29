import pygame as pg 
import sys 

pg.init() 

screen = pg.display.set_mode((1024, 768)) 
color_back = (255, 228, 205) 
screen.fill(color_back) 

clock = pg.time.Clock() 

def gg_moving(pressed, x, y): 
    if pressed[pg.K_w]:  
        if y >= 5: 
            y -= 5 
    if pressed[pg.K_s]:  
        if y <= 743: 
            y += 5 
    if pressed[pg.K_a]:  
        if x >= 5:     
            x -= 3 
    if pressed[pg.K_d]: 
        if x <= 999:  
            x += 3 
    return x, y 

x = 502  
y = 374 
color_gg = (255, 0, 0) 
gg = pg.Rect(x, y, 20, 20) 
pg.draw.rect(screen, color_gg, gg, 0) 

done = False 

while not done: 
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            done = True 

    pressed = pg.key.get_pressed() 
    x, y = gg_moving(pressed, x, y) 
    gg.topleft = (x, y)
    screen.fill(color_back) 
    pg.draw.rect(screen, color_gg, gg, 0) 

    pg.display.flip() 
    clock.tick(30) 

pg.quit()
sys.exit()