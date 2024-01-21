from .Collectable import Collectable
from .CollectableGenerator import CollectableGenerator


class CollectableManager:
	# sets a limit of instances that can exist at the same time of a given type
	MAX_CONTEMPORARY_INSTANCES_PER_TYPE = {"Money": 3, "Life": 1}
	
	def __init__(self):
		self.collectable_generator = CollectableGenerator()
		self.collectables: [Collectable] = []
		self.get_possessed_collectable_types = lambda: [collectable.TYPE for collectable in self.collectables]
		
	def _create_collectables_if_necessary(self):
		for c_type in CollectableGenerator.COLLECTABLE_TYPES.values():
			c_type_count = self.get_possessed_collectable_types().count(c_type)  # number of current collectables of c_type
			if c_type_count < self.MAX_CONTEMPORARY_INSTANCES_PER_TYPE[c_type]:
				# if collectable := self.collectable_generator.create_new_collectable(c_type):
				self.collectables.append(self.collectable_generator.create_new_collectable(c_type))
	
	def update(self, dt):
		[collectable.update(dt) for collectable in self.collectables]
		self.collectables = [collectable for collectable in self.collectables if collectable.is_still_alive()]
		
		self._create_collectables_if_necessary()
		
	def draw_collectables(self, screen):
		[collectable.draw(screen) for collectable in self.collectables]
