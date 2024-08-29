from pygame import Vector2, draw
from circleshape import CircleShape
from constants import BULLET_RADIUS, BULLET_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, BULLET_RADIUS)
        self.rotation = rotation
    def draw(self, screen):
        draw.circle(screen, "#FFFFFF", self.position, self.radius, width=1)
    def update(self, dt):
        velocity = Vector2(0, 1).rotate(self.rotation) * BULLET_SPEED
        self.position += velocity * dt
