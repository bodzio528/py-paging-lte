import unittest
from paginglte.paginglte import is_paging_frame


class PagingFrameTest(unittest.TestCase):
    def test_is_paging_frame(self):
        time = (0, 100, 0)
        ue = {'UEIdentityIndexValue': 100}
        self.assertTrue(is_paging_frame(time, ue))

