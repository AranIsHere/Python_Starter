import unittest

from chp11.name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """能够正确处理像Janis Joplin这样的姓名吗？"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Jains  Joplin')


unittest.main()
