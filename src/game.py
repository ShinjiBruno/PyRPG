import pygame
import sys
from player import Player #".'nome_arquivo'" significa importar do mesmo diretório 

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.player = Player(50, 200)
        self.running=True

    def run(self):
        #loop do jogo
        while self.running:
            self.handle_events()
            self.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.player.update()
        self.draw()
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.player.draw(self.screen)

        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.quit()
