import unittest


class TupleTest(unittest.TestCase):
    def test_compare(self):
        self.assertTrue((0, 0, 0) < (1, 0, 0))
        self.assertTrue((0, 1, 0) < (1, 0, 0))
        self.assertTrue((0, 1, 1) < (1, 0, 0))
        self.assertTrue((0, 1023, 1) < (1, 0, 0))
        self.assertTrue((0, 1023) < (1, 0, 0))


class MainTest(unittest.TestCase):
    from paginglte.paginglte import main
    main()
