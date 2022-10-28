#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Comparaciones básicas sobre el rendimiento de las listas y n-uplets.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from time import time

def test11():
	"""Uso del operador corchete (indice) para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l[1]

def test12():
	"""Uso del operador corchete (indice) para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t[1]

def test21():
	"""Uso del operador corchete (rango) para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l[:]

def test22():
	"""Uso del operador corchete (rango) para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t[:]

def test31():
	"""Uso del método count para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l.count(2)

def test32():
	"""Uso del método count para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t.count(2)

def test41():
	"""Uso del método index para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l.index(2)

def test42():
	"""Uso del método index para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t.index(2)

def test51():
	"""Uso del operador in para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		2 in l

def test52():
	"""Uso del operador in para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		2 in t

def test61():
	"""Uso del operador + para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l + [4, 5, 6]

def test62():
	"""Uso del operador + para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t + (4, 5, 6)

def test71():
	"""Uso del operador * para la lista"""
	l = [1, 2, 3]
	for i in range(10000):
		l * 5

def test72():
	"""Uso del operador * para el n-uplet"""
	t = (1, 2, 3)
	for i in range(10000):
		t * 5

if __name__ == "__main__":
	t0 = time()
	test11()
	t1 = time()
	test12()
	t2 = time()

	print('> corchete')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test21()
	t1 = time()
	test22()
	t2 = time()

	print('> slice')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test31()
	t1 = time()
	test32()
	t2 = time()

	print('> count')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test41()
	t1 = time()
	test42()
	t2 = time()

	print('> index')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test51()
	t1 = time()
	test52()
	t2 = time()

	print('> in')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test61()
	t1 = time()
	test62()
	t2 = time()

	print('> +')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

	print('---------------------')

	t0 = time()
	test71()
	t1 = time()
	test72()
	t2 = time()

	print('> *')
	print('listas : %.10f' % (t1-t0))
	print('tuples : %.10f' % (t2-t1))

