class DynamicArray:
	def __init__(self):
		self.size = 0
		self.elements = []

	def capacity(self):
		return len(self.elements)

	def append(self, item):
		if self.size >= len(self.elements):
			newElements = [0] \
				* max(1, 2 * self.size)

			for i in range(0, self.size):
				newElements[i] = self.elements[i]

			self.elements = newElements

		self.elements[self.size] = item
		self.size += 1

def test(size):
	a = DynamicArray()
	for i in range(0, size):
		a.append(0)

import timeit

with open('impl3_runtime.csv', 'w') as f:
	f.write("x;y\n")
	for m in range(0, 100):
		m = m * 500
		result = ('%d;%.6f\n' % (m, timeit.timeit('test(' + str(m) + ')', setup='from __main__ import DynamicArray, test', number=5))).replace('.', ',')
		print(result)
		f.write(result)
