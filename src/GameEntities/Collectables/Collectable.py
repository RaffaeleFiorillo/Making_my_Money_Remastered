import random
import pygame


class Collectable:
	TYPES = {"coin": "Money", "ingot": "Money", "diamond": "Money", "hp_coin": "Life"}
	APPEARING_PROBABILITY = {"Money": {"coin": 60, "ingot": 19, "diamond": 1},
	                         "Life": {"hp_coin": 10}
	                         }
	VALUES = {"coin": 5, "ingot": 50, "diamond": 5000, "hp_coin": 1}
	LIFE_SPAN = {"coin": 5, "ingot": 7, "diamond": 10, "hp_coin": 6}  # how much they stay on the screen (seconds)
	NAMES = list(VALUES.keys())
	SOUNDS = {name: pygame.mixer.Sound(f"assets/Sounds/{name}.mp3") for name in NAMES}
	
	def __init__(self, x, y, collectable_type):
		self.x = x
		self.y = y
		
		self.type = collectable_type
		self.name = self.get_random_name()
		self.value = self.VALUES[self.name]
		self.life_span = self.LIFE_SPAN[self.name]
		
		self.image = pygame.image.load(f"assets/Images/Collectables/{self.TYPES[self.name]}/{self.name}.png").convert_alpha()
		self.size = tuple(self.image.get_size())
		
		self.get_hitbox = lambda: (self.x, self.y, self.size[0], self.size[1])
		self.hitbox = self.get_hitbox()
		
		self.has_been_collected = False
		self.is_still_alive = lambda: self.life_span >= 0 and not self.has_been_collected
	
	def get_random_name(self):
		total_probability = sum(self.APPEARING_PROBABILITY[self.type].values())
		random_value = random.randint(1, total_probability)
		
		cumulative_probability = 0
		for item, probability in self.APPEARING_PROBABILITY[self.type].items():
			cumulative_probability += probability
			if random_value <= cumulative_probability:
				return item
	
	def apply_collected_effect(self):
		self.has_been_collected = True
		self.SOUNDS[self.name].play()
	
	def update(self, dt):
		self.life_span -= dt
	
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))