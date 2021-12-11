import timeit
import unittest

from utils import get_min, get_max, get_sum, get_multiply, read_numbers_from_file, complex_functionality


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.numbers = [1, 2, 3, -1, 0]
        self.test_file_path = './test.txt'
        self.performance_threshold_100 = 1
        self.performance_threshold_10000 = 5

    def test_read_numbers_from_file(self): # extra test
        with open(self.test_file_path, "w") as input_file:
            input_file.write(' '.join([str(number) for number in self.numbers]))

        self.assertEqual(read_numbers_from_file(self.test_file_path), self.numbers)

    def test_min(self):
        self.assertEqual(get_min(self.numbers), -1)

    def test_max(self):
        self.assertEqual(get_max(self.numbers), 3)

    def test_sum(self):
        self.assertEqual(get_sum(self.numbers), 5)

    def test_multiply(self):
        self.assertEqual(get_multiply(self.numbers), 0)

    def test_speed(self):
        with open(self.test_file_path, "w") as input_file:
            input_file.write(' '.join([str(number) for number in range(100)]))
        perfomance_100 = timeit.timeit(lambda: complex_functionality(self.test_file_path), number = 10000)

        with open(self.test_file_path, "w") as input_file:
            input_file.write(' '.join([str(number) for number in range(10000)]))
        perfomance_10000 = timeit.timeit(lambda: complex_functionality(self.test_file_path), number=1000)

        self.assertLess(perfomance_100, self.performance_threshold_100)
        self.assertLess(perfomance_10000, self.performance_threshold_10000)



if __name__ == '__main__':
    unittest.main()
