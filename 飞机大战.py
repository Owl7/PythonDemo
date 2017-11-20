# -*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time
import random

class BasePlane(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
       	self.y = y
       	self.screen = screen_temp
       	self.image = pygame.image.load(image_name)
       	self.bullet_list = []

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                self.bullet_list.remove(bullet)

class BaseBullet(object):
    def __init__(self, screen_temp, x, y, image_name):
       	self.x = x
       	self.y = y 
       	self.screen = screen_temp
       	self.image = pygame.image.load(image_name)
        
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 40, y - 20, "./source/bullet.png")

    def move(self):
        self.y -= 7

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(BaseBullet):
    def __init__(self, screen_temp, x, y):
        BaseBullet.__init__(self, screen_temp, x + 25, y + 40, "./source/bullet1.png")

    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 852:
            return True
        else:
            return False

class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
       	BasePlane.__init__(self, screen_temp, 210, 700, "./source/hero1.png")

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
    	BasePlane.__init__(self, screen_temp, 0, 0, "./source/enemy0.png")
       	self.direction = "right"

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 480 - 50:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
            
    def fire(self):
        random_num = random.randint(1, 100)
        if random_num == 10 or random_num == 90:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

def key_control(hero_temp):

    #获取事件，比如按键等
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()

def main():

    screen = pygame.display.set_mode((480, 852), 0, 32)
    
    background = pygame.image.load("./source/background.png")

    hero = HeroPlane(screen)

    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))

        hero.display()
        enemy.display()
        enemy.move()    
        enemy.fire()
        key_control(hero)

        pygame.display.update()

        time.sleep(0.01)
            
if __name__ == "__main__":
    main()
