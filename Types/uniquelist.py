#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Definición de una lista de objetos únicos y algunas pruebas unitarias.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


import unittest


class uniquelist(list):
	"""Lista de objetos únicos"""

	def __init__(self, seq=[]):
		"""Sobrecarga genérica del constructor"""
		for value in seq:
			self.append(value)

	def append(self, value):
		"""Sobrecarga del método de adición del elementos al final de la lista"""
		if value not in self:
			list.append(self, value)

	def insert(self, index, value):
		"""Sobrecarga del método de adición del elementos en un índice dado"""
		if value not in self:
			list.insert(self, index, value)

	def extend(self, seq):
		"""sobrecarga del método de modificación de varios elementos"""
		for value in seq:
			self.append(value)

	def __setitem__(self, index, value):
		"""Sobrecarga del método de modificación de un elemento"""
		if value not in self:
			list.__setitem__(self, index, value)

	def __setslice__(self, i, j, seq):
		"""sobrecarga del método de modificación de varios elementos"""
		last = self[j:]
		self.__delslice__(i, j)
		for value in seq:
			if value not in self:
				self.insert(i, value)
				i+=1

	def __add__(self, seq):
		"""sobrecarga del método de adición de varios elementos"""
		checked_seq = []
		for value in seq:
			if value not in self and value not in checked_seq:
				checked_seq.append(value)
		return list.__add__(self, checked_seq)

	def __iadd__(self, seq):
		"""sobrecarga del método de adición de varios elementos"""
		checked_seq = []
		for value in seq:
			if value not in self and value not in checked_seq:
				checked_seq.append(value)
		list.__iadd__(self, checked_seq)
		return self

class uniquelistTest(unittest.TestCase):
	"""Prueba de las listas del elementos únicos"""

	def testConstuct(self):
		self.test = uniquelist([1, 2])
		self.assertEqual(self.test, [1, 2])
		self.test = uniquelist([3, 4, 3])
		self.assertEqual(self.test, [3, 4])

	def testAppend(self):
		self.test = uniquelist()
		self.test.append(5)
		self.assertEqual(self.test, [5])
		self.test.append(6)
		self.assertEqual(self.test, [5, 6])
		self.test.append(6)
		self.assertEqual(self.test, [5, 6])

	def testInsert(self):
		self.test = uniquelist()
		self.test.insert(0, 5)
		self.assertEqual(self.test, [5])
		self.test.insert(1, 6)
		self.assertEqual(self.test, [5, 6])
		self.test.insert(0, 6)
		self.assertEqual(self.test, [5, 6])

	def testExtend(self):
		self.test = uniquelist()
		self.test.extend([5, 7, 9])
		self.assertEqual(self.test, [5, 7, 9])
		self.test = uniquelist()
		self.test.extend([5, 7, 5, 9])
		self.assertEqual(self.test, [5, 7, 9])
		self.test = uniquelist([1])
		self.test.extend([5, 7, 9])
		self.assertEqual(self.test, [1, 5, 7, 9])
		self.test = uniquelist([1])
		self.test.extend([5, 7, 1, 9])
		self.assertEqual(self.test, [1, 5, 7, 9])

	def testSetitem(self):
		self.test = uniquelist([5, 6])
		self.assertEqual(self.test, [5, 6])
		self.test[0] = 1
		self.assertEqual(self.test, [1, 6])
		self.test[0] = 6
		self.assertEqual(self.test, [1, 6])

	def testSetslice(self):
		self.test = uniquelist([1, 2, 3])
		self.assertEqual(self.test, [1, 2, 3])
		self.test[:2] = [5, 4]
		self.assertEqual(self.test, [5, 4, 3])
		self.test[:2] = [5, 4]
		self.assertEqual(self.test, [5, 4, 3])
		self.test[:2] = [0] * 2
		self.assertEqual(self.test, [0, 3])

	def testAdd(self):
		self.test = uniquelist()
		test = self.test + [5, 7, 9]
		self.assertEqual(test, [5, 7, 9])
		self.test = uniquelist()
		test = self.test + [5, 7, 5, 9]
		self.assertEqual(test, [5, 7, 9])
		self.test = uniquelist([1])
		test = self.test + [5, 7, 9]
		self.assertEqual(test, [1, 5, 7, 9])
		self.test = uniquelist([1])
		test = self.test + [5, 7, 1, 9]
		self.assertEqual(test, [1, 5, 7, 9])

	def testIadd(self):
		self.test = uniquelist()
		self.test += [5, 7, 9]
		self.assertEqual(self.test, [5, 7, 9])
		self.test = uniquelist()
		self.test += [5, 7, 5, 9]
		self.assertEqual(self.test, [5, 7, 9])
		self.test = uniquelist([1])
		self.test += [5, 7, 9]
		self.assertEqual(self.test, [1, 5, 7, 9])
		self.test = uniquelist([1])
		self.test += [5, 7, 1, 9]
		self.assertEqual(self.test, [1, 5, 7, 9])

if __name__ == "__main__":
	unittest.main()

