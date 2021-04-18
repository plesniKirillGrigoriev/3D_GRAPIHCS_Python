import pygame
from settings import *
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
# Загружаем фоны
sky = pygame.image.load("sky.jpg")
# Запускаем
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        z += speed
    if keys[pygame.K_s]:
        z -= speed
    if keys[pygame.K_a]:
        x += speed
    if keys[pygame.K_d]:
        x -= speed
    window.blit(sky, (0, 0))
    pygame.draw.line(window, (255, 170, 0), [x, y], [x_end, y_end], z)
    pygame.display.update()
