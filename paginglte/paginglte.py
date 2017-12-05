# -*- coding: utf-8 -*-

"""paginglte.paginglte: provides entry point main()."""

__version__ = "0.1.0"


def make_paging():
    return {
        'UEIdentityIndexValue': 0,
        'UEPagingID': {
            'S-TMSI': {'MME-Code': 0, 'M-TMSI': 0},
            'IMSI': 0
        },
        'PagingDRX': 0,
        'Paging-eDRX-Information': {
            'Paging-eDRX-Cycle': 0,
            'PagingTimeWindow': 0
        }
    }

def make_ue():
    return {
        'UEIdentityIndexValue': 0,
    }


def make_sib():
    return {
        'defaultPagingCycle': 128,
        'nB': 1
    }


HFN = 0
SFN = 1
SubFN = 2


def is_paging_frame(ltetime, ue):
    return ltetime[SFN] % ue['UEIdentityIndexValue'] == 0


def is_drx_cycle(ltetime, sib, ue):
    T = min(ue['UESpecificDRXCycle'], sib['defaultPagingCycle'])
    N = 1 #min(T, nB)
    return ltetime[SFN] % T == (T / N) * (ue['UEIdentityIndexValue'] % N)


def calculate_nearest_paging_occassion(ltetime, sib2, paging):
    T = paging['PagingDRX']
    nB = sib2['nB']
    defaultPagingCycle = sib2['defaultPagingCycle']
    N = min(T, nB)

    rhs = (T / N) * (paging['UEIdentityIndexValue'] % N)
    PagingFrame = ltetime[SFN]


def main():
    print("Hello, LTE Paging Calculator awaits your commands!")


def foo():
    return 34
