import unittest
from credentials import Credentials
class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        set up method that runs before each Test
        '''
        self.new_credentials = Credentials("twitter","billowbashir","123456789")
    def test_init(self):
        self.assertEqual(self.new_credentials.platform_name,"twitter")
        self.assertEqual(self.new_credentials.username,"billowbashir")
        self.assertEqual(self.new_credentials.password,"123456789")
if __name__ =='__main__':
    unittest.main()
