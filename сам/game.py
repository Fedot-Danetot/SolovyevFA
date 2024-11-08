import pygame as pg 
import sys 


pg.init() 


def draw_back():
    '''отвечает за отрисовку окружения'''
    color_back = (255, 228, 205)
    color_border = (205, 178, 155)
    border = pg.Rect(14, 11, 996, 746)
    screen.fill(color_back)
    pg.draw.rect(screen, color_border, border, 3) 


clock = pg.time.Clock() 


def gg_draw(screen, x: int, y: int):
    '''Рисует модельку gg по координатам x, y'''
    gg = pg.Rect(x, y, 20, 20) 
    pg.draw.rect(screen, color_gg, gg, 0)


def gg_moving(x: int, y:int):
    '''Описывает движение игрока (gg)'''
    pressed = pg.key.get_pressed() 
    if pressed[pg.K_w]:  
        if y >= 17: 
            y -= 5 
    if pressed[pg.K_s]:  
        if y <= 731: 
            y += 5 
    if pressed[pg.K_a]:  
        if x >= 18:     
            x -= 5 
    if pressed[pg.K_d]: 
        if x <= 986:  
            x += 5
    return x, y


def enemy_moving(x: int, y: int, e_x: int, e_y: int):
    """Описывает движение врагов"""
    # должны двигаться напрямую к gg
    pass


x = 502  
y = 374 
color_gg = (255, 0, 0)
screen = pg.display.set_mode((1024, 768)) 


def main():
    '''Запускает основной цикл программы'''
    finish = False
    while not finish: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                finish = True
        
        global x; global y
        draw_back()
        x, y = gg_moving(x, y)
        gg_draw(screen, x, y)
        pg.display.flip() 
        clock.tick(30) 

main()
pg.quit()
sys.exit()