from fast_fuzzy_search import FastFuzzySearch
import unittest


class FastFuzzySearchTest(unittest.TestCase):
    def test_add_term(self):
        ffs = FastFuzzySearch()
        ffs.add_term('hello world', 1)
        ffs.add_term('hello friend', 2)

        expected_library = {
            1: 'hello world',
            2: 'hello friend'
        }

        expected_index = {
            (19, 1, 18, 3): set([1, 2]),  # hello
            (1, 18, 3): set([1, 2]),  # hello
            (19, 18, 3): set([1, 2]),  # hello
            (19, 1, 3): set([1, 2]),  # hello
            (19, 1, 18): set([1, 2]),  # hello

            (16, 3, 22, 18, 13): set([1]),  # world
            (3, 22, 18, 13): set([1]),  # world
            (16, 22, 18, 13): set([1]),  # world
            (16, 3, 18, 13): set([1]),  # world
            (16, 3, 22, 13): set([1]),  # world
            (16, 3, 22, 18): set([1]),  # world

            (16, 5, 18, 13): set([1]),  # world
            (5, 18, 13): set([1]),  # world
            (16, 18, 13): set([1]),  # world
            (16, 5, 13): set([1]),  # world
            (16, 5, 18): set([1]),  # world

            (12, 22, 2, 1, 17, 13): set([2]),  # friend
            (22, 2, 1, 17, 13): set([2]),  # friend
            (12, 2, 1, 17, 13): set([2]),  # friend
            (12, 22, 1, 17, 13): set([2]),  # friend
            (12, 22, 2, 17, 13): set([2]),  # friend
            (12, 22, 2, 1, 13): set([2]),  # friend
            (12, 22, 2, 1, 17): set([2]),  # friend

            (12, 22, 7, 17, 13): set([2]),  # friend
            (22, 7, 17, 13): set([2]),  # friend
            (12, 7, 17, 13): set([2]),  # friend
            (12, 22, 17, 13): set([2]),  # friend
            (12, 22, 7, 13): set([2]),  # friend
            (12, 22, 7, 17): set([2]),  # friend
        }

        self.assertDictEqual(ffs.library, expected_library)
        self.assertEqual(len(ffs.index), len(expected_index))
        self.assertDictEqual(ffs.index, expected_index)

    def test_search(self):
        pass


if __name__ == '__main__':
    unittest.main()
