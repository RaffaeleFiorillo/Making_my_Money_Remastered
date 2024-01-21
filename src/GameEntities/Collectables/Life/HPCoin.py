import pygame
from src.GameEntities.Collectables.Collectable import Collectable


class HPCoin(Collectable):
	TYPE = "Life"  # it is important for it to start with upper case
	NAME = "hp_coin"
	VALUE = 1
	IMAGE = pygame.image.load(f"assets/Images/Collectables/{TYPE}/{NAME}.png").convert_alpha()
	SIZE = tuple(IMAGE.get_size())
	SOUND = pygame.mixer.Sound(f"assets/Sounds/{NAME}.mp3")
	
	def __init__(self, x, y):
		super().__init__(x, y, 6)
