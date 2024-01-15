from src.GameEntities.Agents.Enemies.Enemy import Enemy


class EnemyManager:
	ENEMIES_STARTER_COORDINATES = [(0, 0), (930, 580), (0, 580), (930, 0), (465, 584)]
	
	def __init__(self):
		self.enemies: [Enemy] = [Enemy(coo[0], coo[1]) for coo in self.ENEMIES_STARTER_COORDINATES]
		
	def update(self, dt):
		[enemy.update(dt) for enemy in self.enemies]
		
	def draw_enemies(self, screen):
		[enemy.draw(screen) for enemy in self.enemies]
