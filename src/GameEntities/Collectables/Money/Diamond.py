import pygame
from src.GameEntities.Collectables.Collectable import Collectable


class Diamond(Collectable):
	TYPE = "Money"  # it is important for it to start with upper case
	NAME = "diamond"
	VALUE = 5000
	IMAGE = pygame.image.load(f"assets/Images/Collectables/{TYPE}/{NAME}.png").convert_alpha()
	SIZE = tuple(IMAGE.get_size())
	SOUND = pygame.mixer.Sound(f"assets/Sounds/{NAME}.mp3")
	
	def __init__(self, x, y):
		super().__init__(x, y, 10)
