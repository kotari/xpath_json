import unittest
import sys
sys.path[0:0] = ['./xpath_json']
import xpath_json


class TestXpath_Json(unittest.TestCase):
    def setUp(self):
        self.input = {
            "firstName": "John",
            "lastName": "Smith",
            "age": 42,
            "spouse": {
                "firstName": "Mary",
                "lastName": "Smith",
                "age": 40
            },
            "fav.movie": "Mr & Mrs Smith",
            "addresses": [
                {
                    "description": "home",
                    "street": "123 Peachtree Ln",
                    "city": "Atlanta",
                    "state": "GA",
                    "postalCode": 30305
                },
                {
                    "description": "work",
                    "street": "456 Peachtree St",
                    "city": "Atlanta",
                    "state": "GA",
                    "postalCode": 30305
                }
            ],
            "phoneNumbers": [
                {
                    "description": "home",
                    "number": "404-555-1234"
                },
                {
                    "description": "mobile",
                    "number": "678-555-1234"
                }
            ],
            "friends": [
                {"firstName": "Dale", "lastName": "Murphy", "age": 44},
                {"firstName": "Roger", "lastName": "Craig", "age": 68},
                {"firstName": "Jane", "lastName": "Murphy", "age": 47}
            ]
        }
    

    def tearDown(self):
        self.input = None

    
    def test_spouse(self):
        spouse = xpath_json.extract('spouse/firstName', self.input)
        self.assertEqual(spouse, 'Mary')
    
    def test_count_addresses(self):
        count = xpath_json.extract('addresses/#', self.input)
        self.assertEqual(count, 2)

    def test_home_address(self):
        address = xpath_json.extract('addresses/#[description==home]', self.input)
        self.assertDictEqual(address[0], self.input['addresses'][0])

    def test_find_address_by_zipcode(self):
        addresses = xpath_json.extract('addresses/#[postalCode==30305]/#', self.input)
        self.assertEqual(addresses, 2)

    def test_home_phone_number(self):
        phone_number = xpath_json.extract('phoneNumbers/#[description==mobile]/0/number', self.input)
        self.assertEqual(phone_number, '678-555-1234')

    def test_fav_movie(self):
        fav_movie = xpath_json.extract('fav.movie', self.input)
        self.assertEqual(fav_movie, 'Mr & Mrs Smith')

    def test_friends_age_gte_47(self):
        friends = xpath_json.extract('friends/#[age>=47]/#', self.input)
        self.assertEqual(friends, 2)

    def test_friends_age_lt_47(self):
        friends = xpath_json.extract('friends/#[age<47]/#', self.input)
        self.assertEqual(friends, 1)

    def test_friends_first_name(self):
        friends = xpath_json.extract('friends/#/firstName', self.input)
        first_names = ['Dale', 'Roger', 'Jane']
        self.assertListEqual(friends, first_names)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestXpath_Json('test_spouse'))
    suite.addTest(TestXpath_Json('test_count_addresses'))
    suite.addTest(TestXpath_Json('test_home_address'))
    suite.addTest(TestXpath_Json('test_find_address_by_zipcode'))
    suite.addTest(TestXpath_Json('test_home_phone_number'))
    suite.addTest(TestXpath_Json('test_fav_movie'))
    suite.addTest(TestXpath_Json('test_friends_age_gte_47'))
    suite.addTest(TestXpath_Json('test_friends_age_lt_47'))
    suite.addTest(TestXpath_Json('test_friends_first_name'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())