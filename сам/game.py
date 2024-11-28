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
        self.current_player = self.player_model
        self.last_event = None

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
        self.last_event = event
        
        if move_x != 0 and move_y != 0: # вычисление диагонального вектора при нескольких нажатых клавиш
            length = m.sqrt(move_x**2 + move_y**2)
            move_x = (move_x / length) * self.speed
            move_y = (move_y / length) * self.speed

        self.player_model.move_ip(move_x, move_y)
        pg.draw.rect(screen, self.color_player, self.player_model, 0)
        self.current_player = self.player_model # обновление текущего положения игрока


class Enemy:
    def __init__(self):
        self.color_enemy = (255, 0, 0)
        self.enemys = []
        self.create_time = 2000 # время для спавна следующего противника
        self.last_create_time = 0
        self.speed = 5
        self.player = Player() # подгрузка атрибутов и методов класса Player для расчета движения
        self.current_enemys = self.enemys

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
        direction = pg.Vector2(self.player.current_player.center) - pg.Vector2(self.enemys[i].center)
        if direction.length() > 0:
            direction.normalize_ip()
            self.enemys[i].move_ip(direction * self.speed)
        self.current_enemys = self.enemys # обновление текущих положений моделей противников

    def draw(self, i):
        '''Отрисовывает i-ого врага'''
        pg.draw.rect(screen, self.color_enemy, self.enemys[i])


    def kill_player(self, i):
        '''Проверяет касаение моделей игрока и противников'''
        if pg.Rect.colliderect(self.player.current_player, self.enemys[i]):
            # временно
            pg.quit()
            sys.exit()

    def moving_draw_kill(self):
        '''реализует две предыдущих функции для всех врагов'''
        for i in range(len(self.enemys)):
            Enemy.moving(self, i)
            Enemy.draw(self, i)
            Enemy.kill_player(self, i)


class Bullet:
    def __init__(self):
        self.color_bullet = (0, 0, 0)
        self.bullets = []
        self.directions = []
        self.create_time = 1000
        self.last_create_time = -1001 # начальное значение такого чтобы пули спавнились сразу, но это не помогает((
        self.speed = 10
        self.player = Player()
        self.enemy = Enemy()

    def shoot(self): 
        '''Функция для спавна новой пули'''
        current_time = pg.time.get_ticks()  
        event = pg.key.get_pressed()
        if current_time - self.last_create_time > self.create_time: # пули спавнятся с некоторым промежутком времени
            if event[pg.K_UP]: 
                self.directions.append(pg.Vector2(0, -1)) 
                bullet = pg.Rect(*self.player.current_player.midtop, 3, 3) 
                self.bullets.append(bullet) 
            elif event[pg.K_DOWN]: 
                self.directions.append(pg.Vector2(0, 1)) 
                bullet = pg.Rect(*self.player.current_player.midbottom, 3, 3) 
                self.bullets.append(bullet) 
            elif event[pg.K_LEFT]:
                self.directions.append(pg.Vector2(-1, 0)) 
                bullet = pg.Rect(*self.player.current_player.midleft, 3, 3) 
                self.bullets.append(bullet) 
            elif event[pg.K_RIGHT]:
                self.directions.append(pg.Vector2(1, 0)) 
                bullet = pg.Rect(*self.player.current_player.midright, 3, 3) 
                self.bullets.append(bullet)  
            self.last_create_time = current_time

    def moving(self, bul):
        '''Определяет движение снаряда'''
        if len(self.directions) != 0:
            i = self.bullets.index(bul)
            bul.move_ip(self.directions[i] * self.speed)

    def draw(self, bul):
        '''Отрисовывает снаряд'''
        pg.draw.rect(screen, self.color_bullet, bul)

    def kill(self, bul):
        '''Отслеживает коллизию патрона и врага'''
        for enemy_i in self.enemy.current_enemys:
            if pg.Rect.colliderect(bul, enemy_i):
                self.enemy.current_enemys.pop(self.enemy.current_enemys.index(enemy_i))

    def moving_draw_kill(self):
        '''пропускает через три верхних функции каждую пулю'''
        if len(self.bullets) != 0:
            for bul in self.bullets:
                Bullet.moving(self, bul)
                Bullet.draw(self, bul)
                Bullet.kill(self, bul)

clock = pg.time.Clock()

def main():
    '''основной код игры'''
    finish = False
    draw_back()
    # Задаем объекты(?) с помощью классов
    player = Player()
    enemys = Enemy()
    bullets = Bullet()

    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True

        draw_back()
        player.moving()
        
        enemys.player.current_player = player.current_player # обновляет текущее положение игрока для противников
        enemys.spawn()
        enemys.moving_draw_kill()
        
        bullets.enemy.current_enemys = enemys.enemys # обновляет текущее положение противников для пуль
        bullets.player.current_player = player.current_player # обновляет текущее положение игрока для пуль
        bullets.shoot()
        bullets.moving_draw_kill()

        pg.display.flip()
        clock.tick(30)

main()
pg.quit()
sys.exit()