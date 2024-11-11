import pygame as pg 
import random as rnd
import sys


pg.init() 


def draw_back():
        '''отвечает за отрисовку окружения'''
        color_back = (255, 228, 205)
        color_border = (205, 178, 155)
        border = pg.Rect(14, 11, 996, 746)
        screen.fill(color_back)
        pg.draw.rect(screen, color_border, border, 3) 


class Tgg:

    def __init__(self, x, y):
        x = 502  
        y = 374
        self.x = x
        self.y = y
        

    def draw(self, screen):
        '''Рисует модельку gg по координатам x, y'''
        gg = pg.Rect(self.x, self.y, 20, 20) 
        pg.draw.rect(screen, color_gg, gg, 0)


    def moving(self):
        '''Описывает движение игрока (gg)'''
        pressed = pg.key.get_pressed() 
        if pressed[pg.K_w]:  
            if self.y >= 17:    # ограничение для того, чтобы персонаж не выходил за рамки поля
                self.y -= 5 
        if pressed[pg.K_s]:  
            if self.y <= 731: 
                self.y += 5 
        if pressed[pg.K_a]:  
            if self.x >= 18:     
                self.x -= 5 
        if pressed[pg.K_d]: 
            if self.x <= 986:  
                self.x += 5
        return self.x, self.y


class TEnemy:

    def __init__(self):
        pass


    def enemy_spawn():
        '''спавнит врагов раз в какое-то время'''
        pass


    def enemy_moving(x: int, y: int, e_x: int, e_y: int):
        """Описывает движение врагов"""
        # должны двигаться напрямую к gg
        pass


    def enemy_attack():
        '''По сути реализует проигрыш'''
        pass



class TBullet:
    def spawn():
        '''Описывает создание пули'''
        pass

    def moving():
        '''Задает движение пули'''
        pass

    def kills():
        '''Описание сценария "enemy is dead"'''
        pass

 
color_gg = (0, 0, 255)
screen = pg.display.set_mode((1024, 768)) 
clock = pg.time.Clock() 


def main():
    '''Запускает основной цикл программы'''
    finish = False
    Gg = Tgg(502, 374)
    while not finish: 
        for event in pg.event.get(): 
            if event.type == pg.QUIT: 
                finish = True
        
        draw_back()
        Gg.moving()
        Gg.draw(screen)
        pg.display.flip() 
        clock.tick(30)

main()
pg.quit()
sys.exit()