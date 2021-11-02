import unittest
import doctest

class LessonThreeTests(unittest.TestCase):

    def setUp(self):
        ...

    def test_underbar_numbers(self):
        n1 = 1_000_000_000.000_000_1
        n2 = 1000000000.0000001
        self.assertEqual(n1,n2)


    def test_various(self):
        s1 = "Separated they live in the ocean."
        self.assertTrue('they' in s1)
        self.assertTrue(s1.startswith("S"))
        self.assertFalse(s1.endswith("S"))
        self.assertEqual(s1.find('live'), 15)
        self.assertFalse(s1.isnumeric())
        self.assertFalse(s1.isdigit())
        self.assertTrue(s1.isascii())
        s2 = s1.replace("ocean", "river")
        self.assertTrue(s2.endswith("river."))
        lst1 = s1.split(" ")
        self.assertIsInstance(lst1, list)
        self.assertEqual(len(lst1), 6)


    def test_list(self):
        a = [1,2,3,4,5,6,7,8]
        self.assertEqual(a[-2:], [7,8])
        self.assertEqual(a[:4], [1,2,3,4])
        self.assertEqual(a[::-1], [8,7,6,5,4,3,2,1])
        a[4] = "another item"
        self.assertEqual(a, [1,2,3,4,"another item",6,7,8])
        a.append('a new element')
        self.assertEqual(len(a), 9)

    def test_for(self):
        a = [1,2,3,4]
        b = []
        for number in a:
            b.append(number**2)
        self.assertEqual(b, [1,4,9,16])

    def test_square_function(self):
        def square(n):
            return n**2

        self.assertEqual(square(11), 121)
        self.assertEqual(square(5), 25)
        self.assertEqual(square(13), 169)

    def test_for_loop(self):
        vals = []
        for i in range(10):
            vals.append(i**2)
        self.assertEqual(vals, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def test_list_comprehension(self):
        squares = [i**2 for i in range(10)]
        self.assertEqual(squares, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])
        self.assertEqual([letter for letter in 'larry'], ['l', 'a', 'r', 'r', 'y'])

    def test_list_comp_with_func(self):
        price = [120, 230, 319, 241]
        def add_shohizei(p):
            return p * 1.1
        zeikomi = [add_shohizei(p) for p in price]
        self.assertEqual(
            zeikomi,
            [132.0, 253.00000000000003, 350.90000000000003, 265.1]
        )

    def test_complicated_list_comp(self):
        sentence = (
            'The rocket, who was named Ted, came back '
            'from Mars because he missed his friends.'
        )

        def consonant(letter):
            vowels = "aeiou"
            return letter.isalpha() and letter.lower() not in vowels
        consonants = [i for i in sentence if consonant(i)]
        self.assertEqual(consonants, [
            'T','h','r','c','k','t','w',
            'h','w','s','n','m','d','T',
            'd','c','m','b','c','k','f',
            'r','m','M','r','s','b','c',
            's','h','m','s','s','d','h',
            's','f','r','n','d','s'])

if __name__ == '__main__':
    unittest.main()