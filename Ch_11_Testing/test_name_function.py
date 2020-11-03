import unittest

from name_function import get_formatted_name

class NamesTestClass(unittest.TestCase): 
    """Tests for 'name_function.py"""

    def test_first_last_name(self): 
        """Do names like Obi Wan work? """ 
        formatted_name = get_formatted_name('obi', 'wan')
        self.assertEquals(formatted_name, 'Obi Wan')

    def test_first_middle_last(self): 
        """Do middle names work?"""
        formatted_name = get_formatted_name('obi', 'kenobi', 'wan')
        self.assertEquals(formatted_name, 'Obi Wan Kenobi')
    
if __name__ == '__main__': 
    unittest.main()