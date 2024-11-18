import pygame as pg
import sys
import random as rnd
import math as m
pg.init()

screen = pg.display.set_mode((1024, 768))

def draw_back():
    '''отвечает за отрисовку окружения''' 
    color_back = (255, 228, 205)
    color_border = (205, 178, 155)
    border = pg.Rect(14, 11, 996, 746) # граница игрового поля
    screen.fill(color_back)
    pg.draw.rect(screen, color_border, border, 3)
    

class Player:
    def __init__(self):
        '''Автоматически задает свойства модели игрока'''
        self.color_player = (0, 0, 255)
        self.player_model = pg.Rect(502, 374, 20, 20) # моделька игрока - пока квадрат
        self.speed = 6 # скорость игрока
        self.current_player = [502, 374]

    def moving(self):
        '''Отвечает за передвижение модели игрока'''
        move_x, move_y = 0, 0

        event = pg.key.get_pressed()
        if event[pg.K_a] and self.player_model.center[0] > 20: # ограничение движения по границе игрового поля
            move_x = -self.speed
        if event[pg.K_d] and self.player_model.center[0] < 1004:
            move_x = self.speed
        if event[pg.K_s] and self.player_model.center[1] < 756:
            move_y = self.speed
        if event[pg.K_w] and self.player_model.center[1] > 21:
            move_y = -self.speed
        
        if move_x != 0 and move_y != 0: # вычисление диагонального вектора при нескольких нажатых клавиш
            length = m.sqrt(move_x**2 + move_y**2)
            move_x = (move_x / length) * self.speed
            move_y = (move_y / length) * self.speed

        self.player_model.move_ip(move_x, move_y)
        pg.draw.rect(screen, self.color_player, self.player_model, 0)
        self.current_player = self.player_model.center

    def game_over(self):
        '''Реализует проигрыш'''
        # TODO
        pass


class Enemy:
    def __init__(self):
        self.color_enemy = (255, 0, 0)
        self.enemys = []
        self.create_time = 2000
        self.last_create_time = 0
        self.speed = 3
        self.player = Player()

    def spawn(self):
        '''спавнит врагов раз в какое-то время''' 
        current_time = pg.time.get_ticks() 
        if current_time - self.last_create_time > self.create_time: 
            k = rnd.randrange(1, 5) 
            i = self._get_random_position(k) # определяем точку спавна с помощью следующей функции
            enemy = pg.Rect(*i, 20, 20)  
            self.enemys.append(enemy) 
            self.last_create_time = current_time 

    def _get_random_position(self, k):
        '''Случайным образом определяет точку спавна противника'''
        if k == 1: 
            return rnd.randrange(1, 1004, 100), 1 
        elif k == 2: 
            return rnd.randrange(1, 1004, 100), 748 
        elif k == 3: 
            return 1, rnd.randrange(1, 748, 100) 
        elif k == 4: 
            return 1004, rnd.randrange(1, 748, 100)

    def moving(self, i):
        '''Определяет законы движения i-ого врага'''
        direction = pg.Vector2(self.player.current_player) - pg.Vector2(self.enemys[i].center)
        if direction.length() > 0:
            direction.normalize_ip()
            self.enemys[i].move_ip(direction * self.speed)

    def draw(self, i):
        '''Отрисовывает i-ого врага'''
        pg.draw.rect(screen, self.color_enemy, self.enemys[i])


    def moving_draw_all(self):
        '''реализует две предыдущих функции для всех врагов'''
        for i in range(len(self.enemys)):
            Enemy.moving(self, i)
            Enemy.draw(self, i)


clock = pg.time.Clock()

def main():
    finish = False
    draw_back()
    player = Player()
    enemys = Enemy()

    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True

        draw_back()
        player.moving()
        enemys.player.current_player = player.current_player 
        enemys.spawn()
        enemys.moving_draw_all()

        player.game_over()
        pg.display.flip()
        clock.tick(30)

main()
pg.quit()
sys.exit()