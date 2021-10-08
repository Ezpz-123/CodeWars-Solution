from Multiplicationtablefornumber import multi_table
import unittest

import random

class TestMethod(unittest.TestCase):
	def test_base_case(self):
		self.assertEqual(multi_table(5), '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50')
		self.assertEqual(multi_table(1), '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10')

	def test_randomly(self):
		for _ in range(10):
			number = random.randint(-100, 100)
			self.assertEqual(multi_table(number), f'1 * {number} = {number*1}\n2 * {number} = {number*2}\n3 * {number} = {number*3}\n4 * {number} = {number*4}\n5 * {number} = {number*5}\n6 * {number} = {number*6}\n7 * {number} = {number*7}\n8 * {number} = {number*8}\n9 * {number} = {number*9}\n10 * {number} = {number*10}')



if __name__ == '__main__':
	unittest.main()