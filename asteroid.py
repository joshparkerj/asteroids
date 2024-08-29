from circleshape import CircleShape
from pygame import draw

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
    def draw(self, screen):
        draw.circle(screen, "#FFFFFF", self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt


