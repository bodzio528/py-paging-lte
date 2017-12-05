#TODO

## Modus Operandi

py-paging-lte :: ( S1AP Paging , LTE Time )
  -> ( Nearest Paging Occasion LTE Time , Paging Time Window range )

py-paging-lte :: ( Paging Details , LTE Time )
  -> ( Nearest Paging Occasion LTE Time , Paging Time Window range )

Paging Details ::
  -> UEIdentityIndexValue ::= BIT STRING (SIZE (10))
  -> UEPagingID ::= CHOICE { s-TMSI S-TMSI, iMSI IMSI, ... }
    -> S-TMSI ::= SEQUENCE { mMEC MME-Code, m-TMSI M-TMSI ... }
      -> MME-Code ::= OCTET STRING (SIZE (1))
      -> M-TMSI ::= OCTET STRING (SIZE (4))
    -> IMSI ::= OCTET STRING (SIZE (3..8))
  -> PagingDRX ::= ENUMERATED (1..8)
  -> Paging-eDRXInformation ::= SEQUENCE { paging-eDRX-Cycle Paging-eDRX-Cycle, pagingTimeWindow PagingTimeWindow OPTIONAL, ... }
    -> Paging-eDRX-Cycle ::= ENUMERATED{hfhalf, hf1, hf2, hf4, hf8, hf16, hf32, hf64, hf128, hf256, ...}
    -> PagingTimeWindow ::= ENUMERATED{s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s12, s14, s16, s18, s20, ...}

PagingIEs S1AP-PROTOCOL-IES ::= {
{ ID id-UEIdentityIndexValue CRITICALITY ignore TYPE UEIdentityIndexValue PRESENCE mandatory}|
{ ID id-UEPagingID CRITICALITY ignore TYPE UEPagingID PRESENCE mandatory}|
{ ID id-pagingDRX CRITICALITY ignore TYPE PagingDRX PRESENCE optional}|
{ ID id-CNDomain CRITICALITY ignore TYPE CNDomain PRESENCE mandatory}|
{ ID id-TAIList CRITICALITY ignore TYPE TAIList PRESENCE mandatory}|
{ ID id-CSG-IdList CRITICALITY ignore TYPE CSG-IdList PRESENCE optional}|
{ ID id-PagingPriority CRITICALITY ignore TYPE PagingPriority PRESENCE optional}|
{ ID id-UERadioCapabilityForPaging CRITICALITY ignore TYPE UERadioCapabilityForPaging PRESENCE optional}|
-- Extension for Release 13 to support Paging Optimisation and Coverage Enhancement paging --
{ ID id-AssistanceDataForPaging CRITICALITY ignore TYPE AssistanceDataForPaging PRESENCE optional}|
{ ID id-Paging-eDRXInformation CRITICALITY ignore TYPE Paging-eDRXInformation PRESENCE optional}|
{ ID id-extended-UEIdentityIndexValue CRITICALITY ignore TYPE Extended-UEIdentityIndexValue PRESENCE optional},
... }

http://www.sharetechnote.com/html/Paging_LTE.html