import pygame
from src.Utils.GAME_conf import WIDTH, HEIGHT


class Base:
	MAX_SPEED = 360  # pixels/second
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.image = pygame.Surface((64, 64))
		self.size = tuple(self.image.get_size())
		self.speed = [0, 0]  # speed vector at which the entity moves in the current frame
		self.get_hitbox = lambda: (self.x, self.y, self.size[0], self.size[1])
		self.hitbox = self.get_hitbox()
	
	def change_speed_x(self, direction):
		# direction: 1-> go right; 0-> do nothing; -1-> go left
		self.speed[0] = self.MAX_SPEED * direction
	
	def change_speed_y(self, direction):
		# direction: 1-> go down; 0-> do nothing; -1-> go up
		self.speed[1] = self.MAX_SPEED * direction
		
	def update(self, dt):
		self.x += self.speed[0] * dt
		self.y += self.speed[1]  * dt
		
		# Guarantee that an agent does not go outside the screen
		self.x = min(WIDTH - self.size[0], max(0, self.x))
		self.y = min(HEIGHT - self.size[1], max(0, self.y))
		
		self.hitbox = self.get_hitbox()
		
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))
