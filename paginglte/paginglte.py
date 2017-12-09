# -*- coding: utf-8 -*-

"""paginglte.paginglte: provides entry point main()."""

__version__ = "0.1.0"

HFN = 0
SFN = 1
SubFN = 2


def get_pf_index(sib, paging):
    """
    Calculates paging frame index based on SIB2 configuration and incoming S1AP paging.
    Complexity: O(1)

    :rtype: int
    """
    t = min(sib['defaultPagingCycle'], paging['PagingDRX'])
    n = min(t, int(sib['nB'] * t))
    return int((t / n) * (paging['UEIdentityIndexValue'] % n))


def generate_paging_frames(sib, paging, start_time=(0, 0, 0)):
    """
    :param start_time: initial seed for generator
    :param sib: SIB2 configuration
    :param paging: S1AP paging description
    :return: SFN numbers corresponding to Paging Frames
    """
    hfn = start_time[HFN]
    sfn = get_pf_index(sib, paging)
    step = min(sib['defaultPagingCycle'], paging['PagingDRX'])
    while True:
        if (hfn, sfn, 9) >= start_time:
            yield hfn, sfn
        hfn_to_add, sfn = divmod((sfn + step), 1024)
        hfn = (hfn + hfn_to_add) % 1024


def generate_paging_occasions(paging_subframes, pf_generator, end_time):
    """

    :param paging_subframes: generated sunframes UE listens in each Paging Frame
    :param pf_generator:  generator of Paging Framse for specific UE
    :param end_time: last lte time included in list
    :return: generator object, that iterates over consecutive paging occasions
    """
    for start in pf_generator:
        for subframe in paging_subframes:
            po = start + (subframe,)
            if po > end_time:
                return
            if start <= po:
                yield po


def get_paging_subframes(sib, paging):
    t = min(sib['defaultPagingCycle'], paging['PagingDRX'])
    n = min(t, int(sib['nB'] * t))
    ns = int(max(1, sib['nB']))
    i_s = int(paging['UEIdentityIndexValue'] / n) % ns

    if ns == 1:
        return [9]
    elif ns == 2:
        return [[4, 9][i_s]]
    elif ns == 4:
        return [[0, 4, 5, 9][i_s]]


def make_s1ap_paging():
    return {
        'UEIdentityIndexValue': 0,
        'UEPagingID': {
            'S-TMSI': {'MME-Code': 0, 'M-TMSI': 0},
            'IMSI': 0
        },
        'PagingDRX': 128,
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


def make_sib():
    return {
        'defaultPagingCycle': 128,
        'nB': 1.0
    }


def main():
    print("Hello, LTE Paging Calculator awaits your commands!")

    paging = make_s1ap_paging()
    sib = make_sib()

    subframes = get_paging_subframes(sib, paging)
    pf_generator = generate_paging_frames(sib, paging, start_time=(1,0,0))
    po_generator = generate_paging_occasions(subframes, pf_generator, end_time=(3, 128, 8))

    for po in po_generator:
        print(po)
