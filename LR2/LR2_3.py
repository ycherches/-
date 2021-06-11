class my_defaultdict:
	def __init__(self, **kwargs):
		self.elements = dict(kwargs)

	def __repr__(self):
		return str(self.elements)

	def __getitem__(self, key):
		return self.elements[key]

	def __setitem__(self, key, elem):
		self.elements[key] = elem


if __name__ == '__main__':
	test = my_defaultdict(a = 1, b = 2, c = 3)
	print(test)
	print(test['a']) 
	test['d'] = 4
	print(test)
	test['d'] = 5
	print(test)
	print(str(test))