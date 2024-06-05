import pygame
from game import Game

def main():
    # Inicializar o Pygame
    pygame.init()

    game = Game()
    game.run()
    game.quit()

if __name__ == "__main__":
    main()
