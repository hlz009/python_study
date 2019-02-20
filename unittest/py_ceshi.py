import unittest
# from name_function import get_formatted_name

'''
所有以test_打头的方法都会自动测试运行
'''
class NamesTestCase(unittest.TestCase):


    def test_first_last_name(self):
        formatted_name = get_formatted_name("jim", "Green")
        self.assertEqual(formatted_name, "Jim Green")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name("jim", "Green", "Henry")
        self.assertEqual(formatted_name, "Jim Henry Green")

def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()

def get_formatted_name(first, last, middle=None):
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()

unittest.main()