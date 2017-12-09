import unittest

from paginglte.paginglte import get_pf_index

SFN = 1


def make_s1ap_paging(index, drx=128):
    return {
        'UEIdentityIndexValue': index,
        'PagingDRX': drx
    }


class PFIndexTest(unittest.TestCase):
    def test_get_pf_index_nb_two(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': 2.0
        }

        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(0)))
        self.assertEqual(1, get_pf_index(sib, make_s1ap_paging(1)))
        self.assertEqual(2, get_pf_index(sib, make_s1ap_paging(2)))
        self.assertEqual(3, get_pf_index(sib, make_s1ap_paging(3)))

        self.assertEqual(31, get_pf_index(sib, make_s1ap_paging(31)))
        self.assertEqual(32, get_pf_index(sib, make_s1ap_paging(32)))
        self.assertEqual(33, get_pf_index(sib, make_s1ap_paging(33)))

        self.assertEqual(48, get_pf_index(sib, make_s1ap_paging(48)))

        self.assertEqual(63, get_pf_index(sib, make_s1ap_paging(63)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(64)))
        self.assertEqual(1, get_pf_index(sib, make_s1ap_paging(65)))

        self.assertEqual(31, get_pf_index(sib, make_s1ap_paging(63, drx=32)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(64, drx=32)))
        self.assertEqual(1, get_pf_index(sib, make_s1ap_paging(65, drx=32)))

    def test_get_pf_index_nb_half(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': .5
        }

        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(0)))
        self.assertEqual(2, get_pf_index(sib, make_s1ap_paging(1)))
        self.assertEqual(4, get_pf_index(sib, make_s1ap_paging(2)))
        self.assertEqual(6, get_pf_index(sib, make_s1ap_paging(3)))

        self.assertEqual(30, get_pf_index(sib, make_s1ap_paging(15)))
        self.assertEqual(32, get_pf_index(sib, make_s1ap_paging(16)))
        self.assertEqual(34, get_pf_index(sib, make_s1ap_paging(17)))

        self.assertEqual(62, get_pf_index(sib, make_s1ap_paging(31)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(32)))
        self.assertEqual(2, get_pf_index(sib, make_s1ap_paging(33)))

        self.assertEqual(32, get_pf_index(sib, make_s1ap_paging(48)))

        self.assertEqual(62, get_pf_index(sib, make_s1ap_paging(63)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(64)))
        self.assertEqual(2, get_pf_index(sib, make_s1ap_paging(65)))

    def test_get_pf_index_nb_quarter(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': .25
        }

        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(0)))
        self.assertEqual(4, get_pf_index(sib, make_s1ap_paging(1)))
        self.assertEqual(8, get_pf_index(sib, make_s1ap_paging(2)))
        self.assertEqual(12, get_pf_index(sib, make_s1ap_paging(3)))

        self.assertEqual(60, get_pf_index(sib, make_s1ap_paging(15)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(16)))
        self.assertEqual(4, get_pf_index(sib, make_s1ap_paging(17)))

        self.assertEqual(60, get_pf_index(sib, make_s1ap_paging(31)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(32)))
        self.assertEqual(4, get_pf_index(sib, make_s1ap_paging(33)))

        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(48)))

        self.assertEqual(60, get_pf_index(sib, make_s1ap_paging(63)))
        self.assertEqual(0, get_pf_index(sib, make_s1ap_paging(64)))
        self.assertEqual(4, get_pf_index(sib, make_s1ap_paging(65)))
