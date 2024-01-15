import pygame
import random
from src.GameEntities.Agents.BaseAgent import Base
from src.Utils.GAME_conf import WIDTH, HEIGHT


class Enemy(Base):
	IMAGE = pygame.image.load("assets/Images/Enemies/enemy.png").convert_alpha()
	DIRECTIONS = ["up", "down", "left", "right"]
	MAX_SPEED = 320
	SPEEDS = {"up": (0, -1*MAX_SPEED), "down": (0, 1*MAX_SPEED), "left": (-1*MAX_SPEED, 0), "right": (1*MAX_SPEED, 0)}
	
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = self.IMAGE
		self.size = tuple(self.image.get_size())
		self.direction = random.choice(self.DIRECTIONS)
		
		self.time_until_next_choice = 0
		self._get_time_until_next_direction_change()
		self.cannot_change_movement = lambda: self.time_until_next_choice > 0
	
	def _get_time_until_next_direction_change(self):
		# the enemy must wait between 0.2 and 1 seconds before changing direction
		self.time_until_next_choice = random.uniform(0.2, 1)
	
	def _update_speed(self):
		if self.cannot_change_movement():
			return None
		self._get_time_until_next_direction_change()
		
		# if the enemy is near one of the edges of the screen, it goes in the opposite direction
		if self.x + self.size[0] >= WIDTH:
			self.direction = "left"
		elif self.x == 0:
			self.direction = "right"
		elif self.y + self.size[1] >= HEIGHT:
			self.direction = "up"
		elif self.y == 0:
			self.direction = "down"
		else:  # if it is not near the edges, it chooses a random direction
			self.direction = random.choice(self.DIRECTIONS)
		
		self.speed = self.SPEEDS[self.direction]
	
	def update(self, dt):
		self.time_until_next_choice -= dt
		self._update_speed()
		super().update(dt)
