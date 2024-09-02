from circleshape import CircleShape
from pygame import draw
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        draw.circle(screen, "#FFFFFF", self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            new_rotation = random.uniform(20, 50)
            x = self.position[0]
            y = self.position[1]
            radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(x, y, radius, self.velocity.rotate(new_rotation) * 1.2)
            Asteroid(x, y, radius, self.velocity.rotate(-new_rotation) * 1.2)

