import unittest
from city_functions import get_city_info


class CityCountryCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = get_city_info('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')


if __name__ == '__mian__':
    unittest.main()
