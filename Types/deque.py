#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
	A continuación un ejemplo de uso desde un terminal bash:

	$ ./test_deque.py
	listas : 0.0000250340
	deque1 : 0.0000128746
	deque2 : 0.0000071526
	---------------------
	listas : 0.0015981197
	deque1 : 0.0004830360
	deque2 : 0.0004899502
	---------------------
	listas : 0.0490779877
	deque1 : 0.0033481121
	deque2 : 0.0033009052

	A continuación el mismo ejemplo desde una consola Python :

	>>> from test_dequee import *
	>>> main()
	listas : 0.0000250340
	deque1 : 0.0000128746
	deque2 : 0.0000071526
	---------------------
	listas : 0.0015981197
	deque1 : 0.0004830360
	deque2 : 0.0004899502
	---------------------
	listas : 0.0490779877
	deque1 : 0.0033481121
	deque2 : 0.0033009052

"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from collections import deque
from time import time


def test1():
	"""Caso de uso clásico para un buffer
	(FIFO, primero llegar = primero salir)

	Se utiliza simplemente una lista
	"""
	l=[]
	l.insert(0, 1)
	l.insert(0, 2)
	l.pop()
	l.insert(0, 3)
	l.insert(0, 4)
	l.pop()
	l.pop()
	l.insert(0, 5)
	l.pop()
	l.pop()

def test2():
	"""Caso de uso clásico para un buffer
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la derecha
	y vaciado por la la izquierda
	"""
	l = deque()
	l.append(1)
	l.append(2)
	l.popleft()
	l.append(3)
	l.append(4)
	l.popleft()
	l.popleft()
	l.append(5)
	l.popleft()
	l.popleft()

def test3():
	"""Caso de uso clásico para un buffer
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la izquierda
	y vaciado por la la derecha
	"""
	l = deque()
	l.appendleft(1)
	l.appendleft(2)
	l.pop()
	l.appendleft(3)
	l.appendleft(4)
	l.pop()
	l.pop()
	l.appendleft(5)
	l.pop()
	l.pop()

def test11():
	"""Caso de uso de un buffer que primero se llena y luego se vacía
	(FIFO, primero llegar = primero salir)

	Se utiliza simplemente una lista
	"""
	l = []
	for i in range(1000):
		l.insert(0, i)
	for i in range(1000):
		l.pop()

def test12():
	"""Caso de uso de un buffer que primero se llena y luego se vacía
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la derecha
	y vaciado por la la izquierda
	"""
	l = deque()
	for i in range(1000):
		l.append(i)
	for i in range(1000):
		l.popleft()

def test13():
	"""Caso de uso de un buffer que primero se llena y luego se vacía
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la izquierda
	y vaciado por la la derecha
	"""
	l = deque()
	for i in range(1000):
		l.appendleft(i)
	for i in range(1000):
		l.pop()


def test21():
	"""Caso de uso intermediario
	(FIFO, primero llegar = primero salir)

	Se utiliza simplemente una lista
	"""
	l = []
	for j in range(10):
		for i in range(1000):
			l.insert(0, i)
		for i in range(500):
			l.pop()
	for j in range(10):
		for i in range(500):
			l.insert(0, i)
		for i in range(1000):
			l.pop()

def test22():
	"""Caso de uso intermediario de un buffer
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la derecha
	y vaciado por la la izquierda
	"""
	l = deque()
	for j in range(10):
		for i in range(1000):
			l.append(i)
		for i in range(500):
			l.popleft()
	for j in range(10):
		for i in range(500):
			l.append(i)
		for i in range(1000):
			l.popleft()

def test23():
	"""Caso de uso intermediario de un buffer
	(FIFO, primero llegar = primero salir)

	Se utiliza el objeto de relleno por la la izquierda
	y vaciado por la la derecha
	"""
	l = deque()
	for j in range(10):
		for i in range(1000):
			l.appendleft(i)
		for i in range(500):
			l.pop()
	for j in range(10):
		for i in range(500):
			l.appendleft(i)
		for i in range(1000):
			l.pop()

def main():
	"""Lanzamiento de las pruebas y visualización de los resultados"""
	t0 = time()
	test1()
	t1 = time()
	test2()
	t2 = time()
	test3()
	t3 = time()
	print('listas : %.10f' % (t1-t0))
	print('deque1 : %.10f' % (t2-t1))
	print('deque2 : %.10f' % (t3-t2))
	t0 = time()
	test11()
	t1 = time()
	test12()
	t2 = time()
	test13()
	t3 = time()
	print('---------------------')
	print('listas : %.10f' % (t1-t0))
	print('deque1 : %.10f' % (t2-t1))
	print('deque2 : %.10f' % (t3-t2))
	t0 = time()
	test21()
	t1 = time()
	test22()
	t2 = time()
	test23()
	t3 = time()
	print('---------------------')
	print('listas : %.10f' % (t1-t0))
	print('deque1 : %.10f' % (t2-t1))
	print('deque2 : %.10f' % (t3-t2))

if __name__ == "__main__":
	main()

