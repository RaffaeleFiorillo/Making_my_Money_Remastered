import pygame


class Collectable:
	TYPE: str
	NAME: str
	VALUE: int
	IMAGE: pygame.Surface
	SIZE: (int, int)
	SOUND: pygame.mixer.Sound
	
	def __init__(self, x: int, y: int, lifespan: int):
		self.x = x
		self.y = y
		self.lifespan = lifespan  # how much it stays on the screen (seconds)
		self.has_been_collected = False
		self.hitbox = self.get_hitbox()
		
	def get_hitbox(self):
		return self.x, self.y, self.SIZE[0], self.SIZE[1]
	
	def is_still_alive(self):
		return self.lifespan >= 0 and not self.has_been_collected
		
	def apply_collected_effect(self):
		self.has_been_collected = True
		self.SOUND.play()
	
	def update(self, dt):
		self.lifespan -= dt
	
	def draw(self, screen):
		screen.blit(self.IMAGE, (self.x, self.y))
