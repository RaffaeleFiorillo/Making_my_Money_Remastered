import pygame
from src.GameEntities.Collectables.Collectable import Collectable


class Ingot(Collectable):
	TYPE = "Money"  # it is important for it to start with upper case
	NAME = "ingot"
	VALUE = 50
	IMAGE = pygame.image.load(f"assets/Images/Collectables/{TYPE}/{NAME}.png").convert_alpha()
	SIZE = tuple(IMAGE.get_size())
	SOUND = pygame.mixer.Sound(f"assets/Sounds/{NAME}.mp3")
	
	def __init__(self, x, y):
		super().__init__(x, y, 7)
