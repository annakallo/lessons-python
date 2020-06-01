import unittest
from unittest.mock import patch
from unittest_employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass \n')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self): # it runs before every single test
        print('setup')
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)

    def tearDown(self): # it runs after every single test
        print('tear down \n')
        pass
    # this could be used in a case of testing a database in which in the beginning we create some
    # entries but after the test we delete them to have a clean slate

    def test_email(self):
        print('test email')
        # emp_1 = Employee('Corey', 'Schafer', 50000)  # we don't need this anymore cause we have it in the setUp method
        # emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@mail.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@mail.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@mail.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@mail.com')

    def test_fullname(self):
        print('test full name')
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        print('test raise')
        # emp_1 = Employee('Corey', 'Schafer', 50000)
        # emp_2 = Employee('Sue', 'Smith', 60000)

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)


    def test_monthly_schedule(self):
        with patch('unittest_employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Sucess'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Sucess')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()

