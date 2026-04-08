import time 
import random
import math
import pygame
from target_class import Target
pygame.init()

WIDTH, HEIGHT = 800, 600
BG_COLOR = (0, 25, 40)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim-traineR")

TARGET_INCREMENT = 400
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

def draw(window, targets):
    window.fill(BG_COLOR)

    for target in targets:
        target.draw(window)

    pygame.display.update()

def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
        
        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()