import unittest
from city_function import city_country

class CityTestCase(unittest.TestCase): 
    """ Tests for city_function.py """

    def test_city_and_country(self): 
        """ Do city/counties such as 'Madrid' 'Spain' work"""
        f = city_country('madrid','spain')
        self.assertEquals(f, 'Madrid, Spain')

    def test_city_and_country_pop(self): 
        f = city_country('madrid','spain','6.6 million')
        self.assertEquals(f, "Madrid, Spain - Population: 6.6 Million")
if __name__ == '__main__': 
    unittest.main()

