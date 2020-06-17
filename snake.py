import pygame
class snake:
    x = 60
    y = 300
    xdelta = 1
    ydelta = 0
    SCALE = 20

    snake_length = 0
    body = []

    def __init__(self, screen):
        self.screen = screen

    def update(self):
        # update snake body positions
        if self.snake_length != len(self.body):
            for i in range(0, self.snake_length - len(self.body)):
                self.body.append((self.x, self.y))
        else:
            for i in range(0, self.snake_length-1):
                if self.body[i] != self.body[i+1]:
                    self.body[i] = self.body[i+1]
            if self.snake_length > 0:
                self.body[len(self.body)-1] = (self.x, self.y)

        # update x,y of snake head
        self.x += self.xdelta * self.SCALE
        self.y += self.ydelta * self.SCALE

        self.x = self.constrain(self.x, 0, self.screen.get_width()-self.SCALE)
        self.y = self.constrain(self.y, 0, self.screen.get_height()-self.SCALE)

    def show(self):
        # draw head
        # Rect(left, top, width, height)
        square = pygame.Rect(self.x, self.y, self.SCALE, self.SCALE)
        pygame.draw.rect(self.screen, (255, 255, 255), square)

        # draw body
        for segment in self.body:
            square = pygame.Rect(segment[0], segment[1], self.SCALE, self.SCALE)
            pygame.draw.rect(self.screen, (255, 255, 255), square)

    def direction(self, x, y):
        self.xdelta = x
        self.ydelta = y

    def eat(self, food):
        if self.x == food.x and self.y == food.y:
            self.snake_length += food.energy
            return True
        return False

    def crashed(self):
        for segment in self.body:
            if segment[0] == self.x and segment[1] == self.y:
                return True
        return False

    @staticmethod
    def constrain(val, min_val, max_val):
        return min(max_val, max(min_val, val))
