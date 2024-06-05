import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((50,50))
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = 2
    
    #move o jogador
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
    
    def update(self):
        self.move()

    def draw(self, surface):
        surface.blit(self.image, self.rect)