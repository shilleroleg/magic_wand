from random import choice

class Store():
	def __init__(self):
		self.unit = []
		self.price = []

		self.name = ''
		self.full_cost = None

	def _print(self):
		print(f'Нарекаю палочку: {self.name}. Стоимостью {self.full_cost}')

	def _create_name(self):
		for n in self.unit:
			self.name += n

	def _create_price(self):
		self.full_cost = sum(self.price) * 1.25

	def add_item(self, item):
		self.unit.append(item.get_name())
		self.price.append(item.get_price())

	def get_wand(self):
		self._create_name()
		self._create_price() 
		self._print()

	
class Wand():
	def __init__(self, obj_dict):
		self.obj_dict = obj_dict
		self.key = ''
		self.value = None
	
	def _print(self):
		print(self.key, '. Цена - ', self.value)
	
	def set_property(self, key):
		if self.obj_dict.get(key):
			self.key = key
			self.value = self.obj_dict.get(key)
			print('Такой ингредиент есть в наличии. Добавляем: ')
			self._print()
		else:
			self.key = choice(list(self.obj_dict.keys()))
			self.value = self.obj_dict.get(self.key)
			print('Такого ингредиента нет в наличии. Вам подойдет:')
			self._print()

	def get_name(self):
		return self.key

	def get_price(self):
		return self.value

	
if __name__ == '__main__':

	core_dict = {'ус': 10,
			 	'перо': 20,
			 	'волос': 30}
	shield_dict = { 'дуб': 15,
					'береза': 25,
					'ясень': 35}

	# Задаем наполнитель
	core = Wand(core_dict)
	core.set_property('ус')

	# Задаем оболочку
	shield = Wand(shield_dict)
	shield.set_property('дубp')

	# Заходим в магазин
	store = Store()
	store.add_item(core)
	store.add_item(shield)
	# Получаем палочку
	store.get_wand()

