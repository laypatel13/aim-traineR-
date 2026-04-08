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
    clicks = 0
    misses = 0
    start_time = time.time()

    target_pressed = 0

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click = False
        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_position):
                targets.remove(target)
                target_pressed += 1

        draw(WIN, targets)

    pygame.quit()

if __name__ == "__main__":
    main()