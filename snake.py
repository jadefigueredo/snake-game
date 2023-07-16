import pygame
from pygame.locals import *
import random


window_size = (600, 600) # Definindo tamanho da janela 
pixel_size = 10 

def collision(position1, position2):
    return position1 == position2

def off_limits(position):
    if 0<= position[0] < window_size[0] and 0 <= position[1] < window_size[1]:
        return False
    else:
        return True

def random_on_grid():
    x = random.randint(0, window_size[0])
    y = random.randint(0, window_size[1])
    return x // pixel_size * pixel_size, y // pixel_size * pixel_size


pygame.init()
screen = pygame.display.set_mode((window_size))
pygame.display.set_caption("Snake")   # Definindo nome da janela

# Cria elementos do jogo 
snake_position = [(250, 50), (260, 50), (270,50)]
snake_surface = pygame.Surface((pixel_size, pixel_size))
snake_surface.fill((255, 255, 255))

# ponto inicial do jogo
snake_direction = K_LEFT

apple_surface = pygame.Surface((pixel_size, pixel_size))
apple_surface.fill((255, 0, 0))
apple_position = random_on_grid()

def restart_game():
    global snake_position
    global apple_position
    global snake_direction
    snake_position = [(250, 50), (260, 50), (270,50)]
    snake_direction = K_LEFT
    apple_position = random_on_grid


# laço que abre e fecha a janela 
while True: 
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            restart_game()
        elif event.type == KEYDOWN: # Evento de atribuição de controles de teclas
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_position)

    if collision(apple_position, snake_position[0]):
        snake_position.append((-10, -10))
        apple_position = random_on_grid()
    
    for position in snake_position:
        screen.blit(snake_surface, position)
    
    for i in range(len(snake_position)-1, 0, -1):
        if collision(snake_position[0], snake_position[i]):
            pygame.quit()
            restart_game()
        snake_position[i] = snake_position[i-1]

    if off_limits(snake_position[0]):
        pygame.quit()
        restart_game()
    
    if snake_direction == K_UP:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] - pixel_size)
    elif snake_direction == K_DOWN:
        snake_position[0] = (snake_position[0][0], snake_position[0][1] + pixel_size)
    elif snake_direction ==  K_LEFT:
        snake_position[0] = (snake_position[0][0] - pixel_size, snake_position[0][1])    
    elif snake_direction == K_RIGHT:
        snake_position[0] = (snake_position[0][0] + pixel_size, snake_position[0][1])

    pygame.display.update()

