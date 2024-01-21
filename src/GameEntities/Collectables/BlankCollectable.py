import pygame.draw

from src.GameEntities.Collectables.Collectable import Collectable


class Blank(Collectable):
	TYPE = "Blank"  # it is important for it to start with upper case
	NAME = "blank"
	VALUE = 0
	SIZE = (0, 0)
	
	def __init__(self, x, y):
		super().__init__(x, y, 4)
	
	def apply_collected_effect(self):
		self.has_been_collected = True
	
	def draw(self, screen):
		# pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 5, 2)
		pass
