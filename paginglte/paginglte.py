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


def main():
    print("Hello, LTE Paging Calculator awaits your commands!")


def foo():
    return 34
