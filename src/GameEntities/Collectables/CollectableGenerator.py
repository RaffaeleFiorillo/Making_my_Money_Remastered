import random
from .Money.Coin import Coin
from .Money.Ingot import Ingot
from .Money.Diamond import Diamond
from .Life.HPCoin import HPCoin
from .Money.BlankMoney import BlankMoney
from .Life.BlankLife import BlankLife
from src.Utils.GAME_conf import WIDTH, HEIGHT


class CollectableGenerator:
	COLLECTABLE_CLASSES = {"coin": Coin, "ingot": Ingot, "diamond": Diamond, "blankM": BlankMoney,
	                       "hp_coin": HPCoin, "blankL": BlankLife}
	
	COLLECTABLE_TYPES = {col_class.NAME: col_class.TYPE for col_class in COLLECTABLE_CLASSES.values()}
	
	COLLECTABLE_NAMES = list(COLLECTABLE_CLASSES.keys())
	# keep the collectables' order the same as the respective names
	APPEARING_PROBABILITY = {"Money": {"coin": 79, "ingot": 10, "diamond": 1, "blankM": 10},
	                         "Life": {"hp_coin": 20, "blankL": 60}
	                         }
	
	def _get_random_name(self, coll_type):
		# creating a list of all the names that belong to the same type as the given one
		possible_names = [name for name in self.COLLECTABLE_NAMES if self.COLLECTABLE_TYPES[name] == coll_type]
		# creating probability distribution for the names to appear
		probabilities = [v for v in self.APPEARING_PROBABILITY[coll_type].values()]
		name = random.choices(possible_names, probabilities)[0]
		return name
	
	def create_new_collectable(self, collectable_type: str):
		x, y = random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30)
		coll_name = self._get_random_name(collectable_type)
		return self.COLLECTABLE_CLASSES[coll_name](x, y)
