from src.GameEntities.Collectables.BlankCollectable import Blank


class BlankMoney(Blank):
	TYPE = "Money"
	NAME = "blankM"
	
	def __init__(self, x, y):
		super().__init__(x, y)
