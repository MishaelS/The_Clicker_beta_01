from config import FONT_SIZE, HEIGHT, WIDTH, COINS, FPS
from particle import Particles
from coin import Coin
from text import Text
from random import uniform, randint, randrange, choice

import pygame, sys

# -----------------------------------------------------------------------

# Создание частиц
def create_particles(x, y):
	particles_coin.image = pygame.image.load(choice(particles_coin_list)).convert_alpha()
	particles_coin.emit(x, y, uniform(-1, 1), uniform(-1, 1), randint(9, 9*3))

def create_particles_bg(x, y):
	particles_coin_bg.emit(x, y, 0, uniform(1, 3), randint(18, 18*3))

# -----------------------------------------------------------------------

pygame.init()
pygame.display.set_caption('The clicker')
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# -----------------------------------------------------------------------

image_bg = pygame.image.load('img/bg.png').convert_alpha()
rect_bg = image_bg.get_rect(center=(WIDTH/2, HEIGHT/2))

particles_coin_list = ['img/particles_01.png',
					   'img/particles_02.png',
					   'img/particles_03.png']

particles_coin_bg_list = ['img/coins_01.png']

# Создание обьекта монет, тескт и частиц_монет
coin = Coin(screen, 9*20, 9*12)
text = Text(screen, 'font/Minecraft.ttf', FONT_SIZE)
particles_coin = Particles(screen, particles_coin_list, uniform(0.1, 0.5))
particles_coin_bg = Particles(screen, particles_coin_bg_list, uniform(0.07, 0.1))

# -----------------------------------------------------------------------

running = True
while running:
	# Получить fps
	pygame.display.set_caption(f'The clicker {clock.get_fps():2.0f}')
	screen.fill((25, 25, 25))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				# Создание частиц по позиции мыши после нажатия
				mx, my = pygame.mouse.get_pos()
				create_particles(mx, my)
				
				# Проверка на точка столкновения с монетой
				if coin.rect_hit_1.collidepoint(mx, my) or\
				   coin.rect_hit_2.collidepoint(mx, my) or\
				   coin.rect_hit_3.collidepoint(mx, my):
					# Переключение анимации монеты | Переключение масштаба монеты
					coin.switch_click = True
					coin.switch_animation = True
					create_particles_bg(randrange(18, WIDTH - 18, 1), randrange(-18*2, -18*4, -1))
					COINS += 1


	# Обновление монеты
	# Обновление частицы монеты
	# Визуализация текст монеты
	particles_coin_bg.update()
	coin.update()
	particles_coin.update()
	# text.rendering(WIDTH/2, FONT_SIZE*1, f'SECONDS: {coin.seconds:0.2f}', True, (255, 255, 255))

	screen.blit(image_bg, rect_bg)
	text.rendering(WIDTH/2, FONT_SIZE*2, f'COINS: {COINS}', True, (255, 255, 255))

	pygame.display.flip()
	clock.tick(FPS)

# -----------------------------------------------------------------------

pygame.quit()
sys.exit()