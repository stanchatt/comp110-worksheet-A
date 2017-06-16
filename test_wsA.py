import os

if os.environ.get('STRETCH') == 'true':
	def test3():
		assert 2 + 2 == 5

	def test4():
		assert 2 + 2 == 4

	def test5():
		assert 2 + 2 == 6
else:
	def test_two_plus_two():
		assert 2 + 2 == 4

	def test2():
		assert 2 + 2 == 4
