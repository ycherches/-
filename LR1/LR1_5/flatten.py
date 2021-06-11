def flatten_it(it):
	if isinstance(it, dict):
		flatten_dict = []
		for key, value in it.items():
			if value == it:
				raise ValueError('Cyclic refernce detected!')
			else:
				flatten_dict.extend((key, value))
		for el in flatten_it(flatten_dict):
			yield el
	elif hasattr(it, '__iter__') and not isinstance(it, str):
		for elem in it:
			if elem == it:
				raise ValueError('Cyclic refernce detected!')
			else:
				for el in flatten_it(elem):
					yield el
	else:
		yield it


if __name__ == '__main__':
	list_cyclic = [6, 9, 33]
	list_cyclic[2] = list_cyclic
	dict_cyclic = {1: 2, 2: 8, 3: 7}
	dict_cyclic[5] = dict_cyclic
	list_for_testing = [ 
		[3, 67],
		[3, 7, 34, {3, 99}],
		[11, (5, 6)],
		498,
		"678",
		[9, 8, 7],
		(9, [67, 8, (11, 3)], 0, (67, 9)),
		[55, 69, [4, 6]],
		#list_cyclic
		#dict_cyclic
		]
	

	print(test_list)
	print(list(flatten_it(test_list)))
	