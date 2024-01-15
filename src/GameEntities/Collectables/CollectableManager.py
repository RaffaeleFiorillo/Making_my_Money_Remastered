import random
from src.GameEntities.Collectables.Collectable import Collectable
from src.Utils.GAME_conf import WIDTH, HEIGHT


class CollectableManager:
	def __init__(self):
		self.collectables: [Collectable] = []
		self.get_possessed_collectable_types = lambda: [collectable.type for collectable in self.collectables]
	
	def _should_create_more_collectables(self):
		# a collectable can only be created if there are no collectables of the same type
		return len(self.get_possessed_collectable_types()) < 2
	
	def _create_collectable(self, collectable_type: str):
		x, y = random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30)
		self.collectables.append(Collectable(x, y, collectable_type))
	
	def _create_collectables(self):
		possessed_types = self.get_possessed_collectable_types()
		for c_type in Collectable.TYPES.values():
			if c_type not in possessed_types:
				self._create_collectable(c_type)
	
	def update(self, dt):
		[collectable.update(dt) for collectable in self.collectables]
		self.collectables = [collectable for collectable in self.collectables if collectable.is_still_alive()]
		
		if self._should_create_more_collectables():
			self._create_collectables()
	
	def draw_collectables(self, screen):
		[collectable.draw(screen) for collectable in self.collectables]
