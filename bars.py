import pygame

class Bar(pygame.sprite.Sprite):
    def __init__(self, start, height=100, width=5, color=(255,0,0)):

        pygame.sprite.Sprite.__init__(self)

        self.x_position, self.y_position = start[0], start[1]
        self.height = height
        self.width = width
        self.color = color

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.color)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = self.x_position
        self.rect.y = self.y_position
        

class Visualization:

    def __init__(self, screen_side=800, total_bars=75, bar_width=5):

        self.screen_side = screen_side
        self.total_bars = total_bars
        self.bar_width = bar_width

        self.bars = pygame.sprite.Group()

    def make_update_sprites(self, surface, heights=[100]*75):
        self.bars.empty()
        surface.fill((255,255,255))
        x = 10
        y = 600
        for i in range(self.total_bars):
            x += self.bar_width + 5
            self.bars.add(Bar((x, y - heights[i]), heights[i]))
        self.bars.draw(surface)
