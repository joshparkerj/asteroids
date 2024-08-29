from pygame import Vector2
from pygame import draw
from pygame import key
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED
from math import cos, sin, radians

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = Vector2(x, y)
        self.rotation = 180
        print(self)
    def triangle(self):
        forward = Vector2(0, 1).rotate(self.rotation)
        right = Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        draw.polygon(screen, "#FFFFFF", self.triangle(), width=2)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    def move(self, dt):
        self.position = Vector2(
                self.position[0] - PLAYER_SPEED * sin(radians(self.rotation)) * dt,
                self.position[1] + PLAYER_SPEED * cos(radians(self.rotation)) * dt)
    def update(self, dt):
        keys = key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
