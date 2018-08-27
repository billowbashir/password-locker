import unittest
from user import User
class TestContact(unittest.TestCase):
    '''
    testcases below
    '''
    def setUp(self):
        '''
        set up method that runs before each Test
        '''
        self.new_user = User("bashir","billowbashir","123456789")
    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        User.user_list=[]
    def test_init(self):
            self.assertEqual(self.new_user.name,"bashir")
            self.assertEqual(self.new_user.username,"billowbashir")
            self.assertEqual(self.new_user.password,"123456789")

if __name__ =='__main__':
    unittest.main()
