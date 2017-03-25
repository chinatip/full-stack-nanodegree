import unittest
from generate_secret_message import *

class MyTest (unittest.TestCase):    
	def test_getDictionary(self):
		dictionary = getDictionary()          
		self.assertEqual(dictionary, {' ': 'madrid.jpg', '.': 'los angeles.jpg', 'a': 'athens.jpg', 'c': 'bangalore.jpg', 'b': 'austin.jpg', 'e': 'beijing.jpg', 'd': 'barcelona.jpg', 'g': 'bogota.jpg', 'f': 'berkeley.jpg', 'i': 'bucharest.jpg', 'h': 'bristol.jpg', 'k': 'cairo.jpg', 'j': 'buenos aires.jpg', 'm': 'chicago.jpg', 'l': 'chennai.jpg', 'o': 'dallas.jpg', 'n': 'colombo.jpg', 'q': 'edinbrugh.jpg', 'p': 'delhi.jpg', 's': 'houston.jpg', 'r': 'gainesville.jpg', 'u': 'istanbul.jpg', 't': 'hyderabad.jpg', 'w': 'jacksonville.jpg', 'v': 'ithaca.jpg', 'y': 'kiev.jpg', 'x': 'karachi.jpg', 'z': 'london.jpg'})
		self.assertEqual(dictionary.get("m", None), 'chicago.jpg' )
		self.assertEqual(dictionary.get("s", None), 'houston.jpg' )
		self.assertEqual(dictionary.get("v", None), 'ithaca.jpg' )

	def test_manageFolder(self):

		if os.path.exists(newpath):
			list_file = os.listdir(newpath)
			self.assertTrue(len(list_file) == 0 )
			self.assertFalse(len(list_file)> 1)
		else:
			self.assertTrue(os.path.exists(newpath))


if __name__ == '__main__':			
	unittest.main()