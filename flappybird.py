import pygame
import sys

pygame.init()

size = width, height = 288, 512
pipe_size = 100
earth = 404.48

images, sounds = {}, {}

bird = ('data/redbird-upflap.png',
        'data/redbird-midflap.png',
        'data/redbird-downflap.png')

background = 'data/background-day.png'

pipe = 'data/pipe-green.png'

fps = 30
clock = pygame.time.Clock()

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Flappy Bird')

images['score'] = (
    pygame.image.load('data/0.png').convert_alpha(),
    pygame.image.load('data/1.png').convert_alpha(),
    pygame.image.load('data/2.png').convert_alpha(),
    pygame.image.load('data/3.png').convert_alpha(),
    pygame.image.load('data/4.png').convert_alpha(),
    pygame.image.load('data/5.png').convert_alpha(),
    pygame.image.load('data/6.png').convert_alpha(),
    pygame.image.load('data/7.png').convert_alpha(),
    pygame.image.load('data/8.png').convert_alpha(),
    pygame.image.load('data/9.png').convert_alpha())

images['game_over'] = pygame.image.load('data/game_over.png').convert_alpha()

images['start_screen'] = pygame.image.load('data/start_screen.png').convert_alpha()

images['ground'] = pygame.image.load('data/ground.png').convert_alpha()

if 'win' in sys.platform:
    soundExt = '.wav'
else:
    soundExt = '.ogg'

sounds['wing'] = pygame.mixer.Sound('data/wing' + soundExt)
sounds['die'] = pygame.mixer.Sound('data/die' + soundExt)
sounds['hit'] = pygame.mixer.Sound('data/hit' + soundExt)
sounds['point'] = pygame.mixer.Sound('data/point' + soundExt)
sounds['swoosh'] = pygame.mixer.Sound('data/swoosh' + soundExt)

лл
