#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Script que trabaja sobre los números primeros de Mersenne.
"""


__author__ = "Sébastien CHAZALLET"
__copyright__ = "Copyright 2012"
__credits__ = ["Sébastien CHAZALLET", "InsPyration.org", "Ediciones ENI"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Sébastien CHAZALLET"
__email__ = "sebastien.chazallet@laposte.net"
__status__ = "Production"


from sys import stdout
from math import sqrt, log
from time import time


def is_prime ( p ):
	"""Pruebas de primalidad de Lucas-Lehmer"""
	if p == 2: return True
	elif p <= 1 or p % 2 == 0: return False
	for i in range(3, int(sqrt(p))+1, 2 ): 
		if p % i == 0: return False
	return True

def is_mersenne_prime ( p ):
	"""Pruebas de primalidad de Lucas-Lehmer"""
	if p == 2:
		return True
	m_p = ( 1 << p ) - 1
	s = 4
	for i in range(3, p+1): 
		s = (s ** 2 - 2) % m_p
	return s == 0

t0 = time()
precision = 20000
long_bits_width = precision * log(10, 2)
upb_prime = int( long_bits_width - 1 ) // 2
upb_count = 45

print ("Búsqueda de los números primeros de Mersenne para M comprendido entre 2 y %d:" % upb_prime)

count=0
for p in range(2, upb_prime+1): 
	if is_prime(p) and is_mersenne_prime(p):
		print("M%d" % p),
		stdout.flush()
		count += 1
	if count >= upb_count: break

print("Tiempo de ejecución : %.2f" % (time() - t0))

