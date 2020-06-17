import pygame
import random
class food:
    x = 0
    y = 0
    colour = (255, 0, 0)
    energy = 1
    SCALE = 20

    def __init__(self, screen):
        self.screen = screen

    def spawn(self):
        self.x = random.randrange(0, self.screen.get_width()-self.SCALE, self.SCALE)
        self.y = random.randrange(0, self.screen.get_height()-self.SCALE, self.SCALE)

        golden_chance = random.random()
        if golden_chance > 0.5:
            # Golden Apple!
            self.colour = (255, 220, 120)
            self.energy = 5
        else:
            # Regular Apple
            self.colour = (255, 0 ,0)
            self.energy = 1

    def show(self):
        # Rect(left, top, width, height)
        square = pygame.Rect(self.x, self.y, self.SCALE, self.SCALE)
        pygame.draw.rect(self.screen, self.colour, square)

    @staticmethod
    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))
