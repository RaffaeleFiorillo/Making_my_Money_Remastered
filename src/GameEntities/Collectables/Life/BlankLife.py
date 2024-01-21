from src.GameEntities.Collectables.BlankCollectable import Blank


class BlankLife(Blank):
	TYPE = "Life"
	NAME = "blankL"
	
	def __init__(self, x, y):
		super().__init__(x, y)
