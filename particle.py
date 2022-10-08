from random import choice
import pygame

# -----------------------------------------------------------------------

class Particles(pygame.sprite.Sprite):
	def __init__(self, surface, filename, destruction_rate):
		self.image = pygame.image.load(choice(filename)).convert_alpha()
		self.destruction_rate = destruction_rate
		self.surface = surface
		self.particles = []

	def emit(self, x, y, x_vel, y_vel, radius):
		self.particles.append([[x, y], [x_vel, y_vel], radius])

	def update(self):
		for i, particle in reversed(list(enumerate(self.particles))):
			particle[0][0] += particle[1][0]
			particle[0][1] += particle[1][1]
			particle[2] -= self.destruction_rate

			reversed_particle = self.particles[len(self.particles) - i - 1]
			copy_image = pygame.transform.scale(self.image, (reversed_particle[2], reversed_particle[2]))
			self.surface.blit(copy_image, (int(reversed_particle[0][0]), int(reversed_particle[0][1])))
			# pygame.draw.ellipse(screen, (255, 255, 255), (int(reversed_particle[0][0]), int(reversed_particle[0][1]), int(reversed_particle[2]), int(reversed_particle[2])), int(reversed_particle[2]))

			if particle[2] <= 0:
				self.particles.pop(i)