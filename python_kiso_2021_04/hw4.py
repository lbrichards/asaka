import unittest

def is_prime(n):
    # ここでプログラムを書きましょう
    ...

def primes(n):
    # ここでプログラムを書きましょう
    ...


class LessonFourHomeworkTest(unittest.TestCase):

    def test_is_prime(self):

        self.assertTrue(is_prime(1))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(10))


    def test_primes(self):
        p8 = primes(8)
        self.assertTrue(p8, [0, 1, 2, 3, 5, 7, 11, 13])

if __name__ == '__main__':
    unittest.main()