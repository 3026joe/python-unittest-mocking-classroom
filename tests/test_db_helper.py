from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(TestCase):
	def setUp(self):
		pass

	@patch('src.db_helper.DbHelper')
	def test_max_salary_is_greater_than_min_salary(self, MockDbHelper):
		db_helper = MockDbHelper()

		db_helper.get_maximum_salary.return_value = 1000
		db_helper.get_minimum_salary.return_value = 10
		
		max_salary = db_helper.get_maximum_salary()
		min_salary = db_helper.get_minimum_salary()
		self.assertGreater(max_salary, min_salary)