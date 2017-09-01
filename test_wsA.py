# Do not edit, rename or delete this file!

import pytest
import os
import sqlite3
import glob

connection = None
connection_error = None

# Find the database file by wildcard matching
filenames = glob.glob('*.user')
if len(filenames) < 1:
	connection_error = "Save file was not found"
elif len(filenames) > 1:
	connection_error = "Multiple save files were found"
else:
	connection = sqlite3.connect(filenames[0])
	connection.row_factory = sqlite3.Row
	
def test_connection():
	assert connection_error is None, connection_error
	assert connection is not None


def get_level_row(level_id):
	c = connection.cursor()
	c.execute('''SELECT * FROM Level WHERE id=?''', (level_id,))
	return c.fetchone()


which_tests = os.getenv('TEST_SET', 'core')

if which_tests == 'core':
	levels = [
		("research-example-1", "Of Pancakes and Spaceships"),
		("research-tutorial-1", "Slightly Different"),
		("research-tutorial-1point5", "Crossover"),
		("research-example-2", "An Introduction to Bonding"),
		("research-tutorial-2", "A Brief History of SpaceChem"),
		("research-tutorial-3", "Removing Bonds"),

		("research-tutorial-4", "Double Bonds"),
		("research-tutorial-5", "Best Left Unanswered"),
		("research-tutorial-6", "Multiple Outputs"),
		("production-tutorial-1", "An Introduction to Pipelines"),
		("production-tutorial-2", "There's Something in the Fishcake"),
		("production-tutorial-3", "Sleepless on Sernimir IV"),

		("bonding-2", "Every Day is the First Day"),
		("bonding-3", "It Takes Three"),
		("bonding-4", "Split Before Bonding"),
		("bonding-6", "Settling into the Routine"),
		("bonding-7", "Nothing Works"),
		# ("bonding-boss", "A Most Unfortunate Malfunction"),
		# ("bonding-5", "Challenge: In-Place Swap")
	]
		
	@pytest.mark.parametrize("level_id,level_friendly_name", levels)
	def test_level_completed(level_id, level_friendly_name):
		row = get_level_row(level_id)
		assert row is not None, "'%s' has not been attempted" % level_friendly_name
		assert row['passed'] != 0, "'%s' has not been passed" % level_friendly_name

elif which_tests == 'stretch_a':
	def test_everyday_300():
		row = get_level_row('bonding-2')
		assert row is not None, "'Every Day is the First Day' has not been attempted"
		assert row['passed'] != 0, "'Every Day is the First Day' has not been passed"
		assert row['cycles'] <= 300

elif which_tests == 'stretch_b':
	def test_ittakes_20():
		row = get_level_row('bonding-3')
		assert row is not None, "'It Takes Three' has not been attempted"
		assert row['passed'] != 0, "'It Takes Three' has not been passed"
		assert row['symbols'] <= 20

elif which_tests == 'stretch_c':
	levels = [
		("bonding-5", "Challenge: In-Place Swap"),
		("sensing-1", "An Introduction to Sensing"),
		("sensing-2", "Prelude to a Migraine"),
		("sensing-3", "Random Oxides"),
	]
		
	@pytest.mark.parametrize("level_id,level_friendly_name", levels)
	def test_level_completed(level_id, level_friendly_name):
		row = get_level_row(level_id)
		assert row is not None, "'%s' has not been attempted" % level_friendly_name
		assert row['passed'] != 0, "'%s' has not been passed" % level_friendly_name
