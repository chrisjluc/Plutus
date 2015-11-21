import unittest
from category import StringContainsAll, Category

class StringContainsAllTests(unittest.TestCase):

    def test_one_arg_match(self):
        self.assertTrue(StringContainsAll('hello').is_match('HELLO HOW ARE YOU'))

    def test_one_arg_no_match(self):
        self.assertFalse(StringContainsAll('hello').is_match('ELLO HOW hell ARE YOU'))

    def test_two_arg_match(self):
        self.assertTrue(StringContainsAll('hello', 'you').is_match('HELLO HOW ARE YOU'))

    def test_two_arg_no_match(self):
        self.assertFalse(StringContainsAll('hell', 'your').is_match('ELLO HOW hell ARE YOU'))


class TestCategory(Category):
    match_candidates = [
            StringContainsAll('uber'),
            StringContainsAll('lyft', 'ride'),
    ]


class CategoryTests(unittest.TestCase):

    def test_category_match(self):
        test_category = TestCategory()
        self.assertTrue(test_category.belongs_to_category('UBER TECHNOLOGIES'))

    def test_category_no_match(self):
        test_category = TestCategory()
        self.assertFalse(test_category.belongs_to_category('LYFT'))



if __name__ == '__main__':
    unittest.main()
