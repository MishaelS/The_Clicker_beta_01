from config import WIDTH, HEIGHT
import pygame

# -----------------------------------------------------------------------

# Класс монет
class Coin(pygame.sprite.Sprite):
	def __init__(self, surface, size_max, size_min):
		self.image_list = [pygame.image.load('img/coins_01.png').convert_alpha(),
						   pygame.image.load('img/coins_02.png').convert_alpha(),
						   pygame.image.load('img/coins_03.png').convert_alpha()]
		self.size_max = size_max
		self.size_min = size_min
		self.angle = self.size_max
		self.seconds = 0.0
		self.surface = surface
		self.speed_second = 0.005
		self.switch_scale = True
		self.switch_click = False
		self.switch_animation = False
		self.switch_image(self.image_list, 0)
		self.collision_rect()

	# Переключатель картинки
	def switch_image(self, image, index):
		self.image_old = image[index]
		self.image_old = pygame.transform.scale(self.image_old, (self.size_max, self.size_max))
		self.rect_old = self.image_old.get_rect(center=(WIDTH/2, HEIGHT/2))

	# Cтолкновение картинки
	def collision_rect(self):
		self.image_hit_1 = pygame.Surface((self.size_max-80,    self.size_max))
		self.image_hit_2 = pygame.Surface((   self.size_max, self.size_max-80))
		self.image_hit_3 = pygame.Surface((self.size_max-40, self.size_max-40))

		self.rect_hit_1 = self.image_hit_1.get_rect(center=self.rect_old.center)
		self.rect_hit_2 = self.image_hit_2.get_rect(center=self.rect_old.center)
		self.rect_hit_3 = self.image_hit_3.get_rect(center=self.rect_old.center)

	# Анимации с таймером
	def animations(self):
		self.seconds += self.speed_second
		angle = 0.02
		if self.seconds >= angle and self.seconds <= angle*2:
			self.switch_image(self.image_list, 1)
		elif self.seconds >= angle*2 and self.seconds <= angle*3:
			self.switch_image(self.image_list, 2)
		elif self.seconds >= angle*3 and self.seconds <= angle*4:
			self.switch_image(self.image_list, 1)
		elif self.seconds >= angle*4 and self.seconds <= angle*5:
			self.switch_image(self.image_list, 0)
			self.switch_animation = False
			self.seconds = 0.0

	# Анимация маштабирования
	def animation_scale(self):
		speed_rotate = 12.0
		if self.switch_scale:
			if self.angle <= self.size_max and self.angle >= self.size_min:
				self.angle -= speed_rotate
			elif self.angle <= self.size_min:
				self.angle = self.size_min
				self.switch_scale = False
		else:
			self.angle += speed_rotate
			if self.angle >= self.size_max:
				self.angle = self.size_max
				self.switch_scale = True
				self.switch_click = False
		self.scale_image(self.angle)

	# Маштабирование картинки
	def scale_image(self, size):
		self.image = pygame.transform.scale(self.image_old, (size, size))
		self.rect = self.image.get_rect(center=self.rect_old.center)

	# Обновление обьекта
	def update(self):
		if self.switch_animation:
			self.animations()
		if self.switch_click:
			self.animation_scale()

		self.scale_image(self.angle)
		self.surface.blit(self.image, self.rect)

		# self.surface.blit(self.image_old, self.rect_old)
		# self.surface.blit(self.image_hit_1, self.rect_hit_1)
		# self.surface.blit(self.image_hit_2, self.rect_hit_2)
		# self.surface.blit(self.image_hit_3, self.rect_hit_3)