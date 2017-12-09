import unittest
from paginglte.paginglte import generate_paging_frames, generate_paging_occasions, get_paging_subframes

HFN = 0
SubFN = 2


class GeneratePagingFramesTest(unittest.TestCase):
    def test_generate_first_paging_occasions_for_ue_id_0(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': 2.0
        }

        paging = {
            'UEIdentityIndexValue': 0,
            'PagingDRX': 64
        }

        generator = generate_paging_frames(sib, paging)
        self.assertEqual((0, 0), next(generator))
        self.assertEqual((0, 64), next(generator))
        self.assertEqual((0, 128), next(generator))
        self.assertEqual((0, 192), next(generator))
        self.assertEqual((0, 256), next(generator))

    def test_generate_first_paging_occasions_for_ue_id_1(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': 2.0
        }

        paging = {
            'UEIdentityIndexValue': 1,
            'PagingDRX': 64
        }

        generator = generate_paging_frames(sib, paging)
        self.assertEqual((0, 1), next(generator))
        self.assertEqual((0, 65), next(generator))
        self.assertEqual((0, 129), next(generator))
        self.assertEqual((0, 193), next(generator))
        self.assertEqual((0, 257), next(generator))

    def test_generate_first_paging_occasions_for_ue_id_1_and_nb_half(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': .5
        }

        paging = {
            'UEIdentityIndexValue': 1,
            'PagingDRX': 64
        }

        generator = generate_paging_frames(sib, paging)
        self.assertEqual((0, 2), next(generator))
        self.assertEqual((0, 66), next(generator))
        self.assertEqual((0, 130), next(generator))
        self.assertEqual((0, 194), next(generator))
        self.assertEqual((0, 258), next(generator))

    def test_generate_first_paging_occasions_for_ue_id_1_and_nb_half_and_paging_dex_32(self):
        sib = {
            'defaultPagingCycle': 64,
            'nB': .5
        }

        paging = {
            'UEIdentityIndexValue': 1,
            'PagingDRX': 32
        }

        generator = generate_paging_frames(sib, paging)
        self.assertEqual((0, 2), next(generator))
        self.assertEqual((0, 34), next(generator))
        self.assertEqual((0, 66), next(generator))
        self.assertEqual((0, 98), next(generator))
        self.assertEqual((0, 130), next(generator))

    def test_generate_first_paging_occasions_for_ue_id_0_and_drx_cycle_512(self):
        sib = {
            'defaultPagingCycle': 512,
            'nB': 4.0
        }

        paging = {
            'UEIdentityIndexValue': 0,
            'PagingDRX': 512
        }

        generator = generate_paging_frames(sib, paging)
        self.assertEqual((0, 0), next(generator))
        self.assertEqual((0, 512), next(generator))
        self.assertEqual((1, 0), next(generator))
        self.assertEqual((1, 512), next(generator))
        self.assertEqual((2, 0), next(generator))


class PagingSubframesTest(unittest.TestCase):
    def test_get_paging_subframes_case1(self):
        sib = {
            'defaultPagingCycle': 256,
            'nB': 4.0
        }

        paging = {
            'UEIdentityIndexValue': 147,
            'PagingDRX': 256
        }

        self.assertEqual([0], get_paging_subframes(sib, paging))

    def test_get_paging_subframes_case2(self):
        sib = {
            'defaultPagingCycle': 256,
            'nB': 2.0
        }

        paging = {
            'UEIdentityIndexValue': 148,
            'PagingDRX': 128
        }

        self.assertEqual([9], get_paging_subframes(sib, paging))

    def test_get_paging_subframes_case3(self):
        sib = {
            'defaultPagingCycle': 256,
            'nB': .5
        }

        paging = {
            'UEIdentityIndexValue': 276,
            'PagingDRX': 128
        }

        self.assertEqual([9], get_paging_subframes(sib, paging))


class GeneratePagingOccasionsTest(unittest.TestCase):
    def test_example1(self):
        expected_frames = [(0, 0, 4), (0, 0, 9), (0, 64, 4), (0, 64, 9), (0, 128, 4), (0, 128, 9), (0, 192, 4),
                           (0, 192, 9)]
        end_time = (0, 192, 9)

        paging_subframes = [4, 9]
        pf_generator = ((0, x) for x in range(0, 1024, 64))

        self.assertEqual(expected_frames,
                         [x for x in generate_paging_occasions(paging_subframes, pf_generator, end_time)])
