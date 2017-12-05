from unittest import TestCase


class EmptyTest(TestCase):
    def test_foo(self):
        from paginglte import paginglte as mut
        self.assertEqual(mut.foo(), 34)