import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen: pygame.Surface, color: str = "white") -> pygame.draw.circle:
        return pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float):
        self.position += (self.velocity * dt)