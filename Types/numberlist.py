#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Definición de una lista de enteros y algunas pruebas unitarias.
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


class numberlist(list):
	"""Lista de números"""

	__types__ = [type(0), type(0.)]

	def __init__(self, seq=[]):
		"""Sobrecarga genérica del constructor"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("el objeto %s de índice %s de la secuencia no es un número" % (value, index))
		list.__init__(self, seq)

	def append(self, value):
		"""Sobrecarga del método de adición del elementos al final de la lista"""
		if type(value) not in self.__types__:
			raise TypeError("%s no es un número" % value)
		list.append(self, value)

	def insert(self, index, value):
		"""Sobrecarga del método de adición del elementos en un índice dado"""
		if type(value) not in self.__types__:
			raise TypeError("%s no es un número" % value)
		list.insert(self, index, value)

	def extend(self, seq):
		"""sobrecarga del método de modificación de varios elementos"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("el objeto %s de índice %s de la secuencia no es un número" % (value, index))
		list.extend(self, seq)

	def __setitem__(self, index, value):
		"""Sobrecarga del método de modificación de un elemento"""
		if type(value) not in self.__types__:
			raise TypeError("%s no es un número" % value)
		list.__setitem__(self, index, value)

	def __setslice__(self, i, j, seq):
		"""sobrecarga del método de modificación de varios elementos"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("el objeto %s de índice %s de la secuencia no es un número" % (value, index))
		list.__setslice__(self, i, j, seq)

	def __add__(self, seq):
		"""sobrecarga del método de adición de varios elementos"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("el objeto %s de índice %s de la secuencia no es un número" % (value, index))
		return list.__add__(self, seq)

	def __iadd__(self, seq):
		"""sobrecarga del método de adición de varios elementos"""
		for index, value in enumerate(seq):
			if type(value) not in self.__types__:
				raise TypeError("el objeto %s de índice %s de la secuencia no es un número" % (value, index))
		list.__iadd__(self, seq)
		return self

class numberlistTest(unittest.TestCase):
	"""Pruebas de las listas de números"""

	def testConstuct(self):
		self.test = numberlist([1, 2.])
		self.assertEqual(self.test, [1, 2.])
		self.assertRaises(TypeError, numberlist, ['7'])

	def testAppend(self):
		self.test = numberlist()
		self.test.append(5)
		self.assertEqual(self.test, [5])
		self.test.append(6.)
		self.assertEqual(self.test, [5, 6.])
		self.assertRaises(TypeError, self.test.append, '7')

	def testInsert(self):
		self.test = numberlist()
		self.test.insert(0, 5)
		self.assertEqual(self.test, [5])
		self.test.insert(1, 6.)
		self.assertEqual(self.test, [5, 6.])
		self.assertRaises(TypeError, self.test.append, '7')

	def testExtend(self):
		self.test = numberlist()
		self.test.extend([5, 7, 9.])
		self.assertEqual(self.test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.extend, [5, '7', 9.])
		self.assertEqual(self.test, [5, 7, 9.])

	def testSetitem(self):
		self.test = numberlist([5])
		self.assertEqual(self.test, [5])
		self.test[0] = 1
		self.assertEqual(self.test, [1])
		self.assertRaises(TypeError, self.test.__setitem__, 0, '7')

	def testSetslice(self):
		self.test = numberlist([1, 2, 3])
		self.assertEqual(self.test, [1, 2, 3])
		self.test[:2] = [0] *2
		self.assertEqual(self.test, [0, 0, 3])
		self.assertRaises(TypeError, self.test.__setslice__, 0, 2, [1, '7'])

	def testAdd(self):
		self.test = numberlist()
		test = self.test + [5, 7, 9.]
		self.assertEqual(test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.__add__, [5, '7', 9.])
		self.assertEqual(self.test, [])

	def testIadd(self):
		self.test = numberlist()
		self.test += [5, 7, 9.]
		self.assertEqual(self.test, [5, 7, 9.])
		self.assertRaises(TypeError, self.test.__iadd__, [5, '7', 9.])
		self.assertEqual(self.test, [5, 7, 9.])

if __name__ == "__main__":
	unittest.main()

