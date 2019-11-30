import sys
import time
import requests
import json

from BO.Poke import Pokemon

import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Pykemon")

    screen = pygame.display.set_mode((500,500))

    image = pygame.image.load("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/1.png")

    screen.blit(image, (50,50))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
        