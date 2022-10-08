import pygame

# -----------------------------------------------------------------------

# Класс текст
class Text:
	def __init__(self, surface, font, size):
		self.font = pygame.font.Font(font, size)
		self.surface = surface
		self.size = size

	# Отрисовка обьекта
	def rendering(self, x, y, text, antialias, color):
		render_text = self.font.render(text, antialias, color)
		rect_text = render_text.get_rect(center=(x, y))
		self.surface.blit(render_text, rect_text)
