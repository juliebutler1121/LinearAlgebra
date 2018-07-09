##########################################################################################
# LinearAlgebra.py
# Julie Butler
# Version 1.0
# July 9th, 2018
#
# A colection of methods that perform linear algebra related calculations.  The code is
# split into different classes by topic/subject.
##########################################################################################

##########################################################################################
# CLASSES:
# quantumMechanics: methods that are especially perternate to quantum mechanics 
#	calculations 
# linearAlgebra: basic linear algebra calculations that are not included in numpy or that
#	needed to be modified from the numpy versions
##########################################################################################

##################################################
#
#                 IMPORTS
#
##################################################
# Allows for the use of effecient arrays and must basic linear algebra calculations
import numpy as np 
# Commonly used methods from the numpy library 
from numpy import dot

##################################################
#
#              quantumMechanics
#
# Methods:
# commutator: takes in two numpy arrays and returns the commutator of them, which is
#	defined as AB-BA.
# nestedCommutator: takes in two numpy arrays and an integer and performs the nested
#	commutator [a, b]^(n), where [a, b]^(n) = [a, [a, b]^(n-1)] and 
#	[a, b]^(0) = b
##################################################

class quantumMechanics:
	##################################################
	#
	#                   __init__
	#
	##################################################
	def __init__ (self, array1, array2):
		"""
		Input:
			array1 (a numpy array): one of the arrays to perform 
				calculations on
			array2 (a numpy array): the other array to perform calculations
				on
		Output:
			None.
			
		Initializes the class level numpy arrays a and b to the inputted numpy
		arrays.  Order matters in these calculations so the order of array1 and
		array2 matter.
		"""
		self.a = array1
		self.b = array2
	
	##################################################
	#
	#                  commutator
	#
	##################################################
	def commutator (self):
		"""
		Input:
			None.
		Output:
			Unnamed (a double): the result of the commutator being
				performed on class level numpy arrays a and b
		
		Performs a commutator on the class level numpy arrays a and b, i.e
		returns the value of AB - BA.
		"""
		return dot (a, b) - dot (b, a)
	
	##################################################
	#
	#              nestedCommutator
	#
	##################################################
	def nestedCommutator (self, n):
		"""
		Input:
			n (an integer): the number of times the nested commutator routine
				is to be performed.
		Output:
			Unnamed (a double): The result of performing the nested commutator n
				times on class level numpy arrays a and b.
				
		Performs a nested commutator with n iterations on teh class level numpy arrays
			a and b.  For the nested commutator [a, b]^(n) = [a, [a, b]^(n-1)] and
			[a, b]^(0) = b.
		"""
		if n == 0:
			return b
		else:
			return commutator (a, nestedCommutator (a, b, n-1))
		