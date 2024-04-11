# For running client against PAT host
# See also: expected_dev1.py   (SP DEV)

all_fields = [
    "data_release",
    "datasetgroup",
    "dateobs",
    "dateobs_center",
    "dec",
    "exptime",
    "flux",
    "instrument",
    "ivar",
    "mask",
    "model",
    "ra",
    "redshift",
    "redshift_err",
    "redshift_warning",
    "site",
    "sparcl_id",
    "specid",
    "specprimary",
    "spectype",
    "survey",
    "targetid",
    "telescope",
    "wave_sigma",
    "wavelength",
    "wavemax",
    "wavemin",
]


default_fields = ["dec", "flux", "ra", "sparcl_id", "specid", "wavelength"]

# OLD as of Dec 14, 2023
# retrieve_0 = [1254334738051655680, 1254335012929562624]

retrieve_0 = [39627920993422590, 39627926995470031]

retrieve_0b = ["_dr", "dec", "flux", "ra", "sparcl_id", "specid", "wavelength"]

# OLD as of Dec 14, 2023
# retrieve_5 = [1254334738051655680, 1254335012929562624]

retrieve_5 = [39627920993422590, 39627926995470031]

# OLD as of Dec 14, 2023
# find_0 = [
#    {
#        "_dr": "BOSS-DR16",
#        "dec": 28.038113,
#        "ra": 132.95902999999998,
#        "sparcl_id": "611a5a1c-75d8-11ee-8b9f-525400aad0aa",
#    },
#    {
#        "_dr": "BOSS-DR16",
#        "dec": 28.019856,
#        "ra": 132.93685,
#        "sparcl_id": "61357ba4-75d8-11ee-a1b5-525400aad0aa",
#    },
# ]

find_0 = [
    {
        "_dr": "BOSS-DR16",
        "dec": 3.4911852,
        "ra": 340.93613000000005,
        "sparcl_id": "0c46e982-992d-11ee-b800-525400aad0aa",
    },
    {
        "_dr": "BOSS-DR16",
        "dec": 3.0464991,
        "ra": 340.93298000000004,
        "sparcl_id": "2602c4a5-992d-11ee-b3e7-525400aad0aa",
    },
]

# OLD as of Dec 14, 2023
# find_1 = [
#    {
#        "_dr": "SDSS-DR17",
#        "dec": -0.98681,
#        "ra": 313.90848,
#        "sparcl_id": "0002f55c-75d7-11ee-822f-525400aad0aa",
#    }
# ]

find_1 = [
    {
        "_dr": "DESI-EDR",
        "dec": 5.662937176455572,
        "ra": 208.7076645721256,
        "sparcl_id": "00063e73-992e-11ee-ad57-525400aad0aa",
    }
]

find_2 = 936894  # PAT

# OLD as of Dec 14, 2023
# find_3 = [
#    {
#        "_dr": "SDSS-DR17",
#        "dec": -0.98681,
#        "ra": 313.90848,
#        "sparcl_id": "0002f55c-75d7-11ee-822f-525400aad0aa",
#    },
#    {
#        "_dr": "SDSS-DR17",
#        "dec": -0.945676,
#        "ra": 313.91043,
#        "sparcl_id": "000df610-75d7-11ee-9957-525400aad0aa",
#    },
#    {
#        "_dr": "SDSS-DR17",
#        "dec": -0.486388,
#        "ra": 313.70407,
#        "sparcl_id": "0018f253-75d7-11ee-8253-525400aad0aa",
#    },
# ]

# OLD as of March 13, 2024
# find_3 = [{'_dr': 'DESI-EDR',
#           'dec': 5.662937176455572,
#           'ra': 208.7076645721256,
#           'sparcl_id': '00063e73-992e-11ee-ad57-525400aad0aa'},
#          {'_dr': 'DESI-EDR',
#           'dec': 5.492057016906403,
#           'ra': 209.52823969727436,
#           'sparcl_id': '000d4892-9931-11ee-9e4d-525400aad0aa'},
#          {'_dr': 'SDSS-DR17',
#           'dec': 34.863511,
#           'ra': 194.86904,
#           'sparcl_id': '000e388f-992d-11ee-a373-525400aad0aa'}]

find_3 = [
    {
        "_dr": "DESI-EDR",
        "dec": 5.662937176455572,
        "ra": 208.7076645721256,
        "sparcl_id": "00063e73-992e-11ee-ad57-525400aad0aa",
    },
    {
        "_dr": "DESI-EDR",
        "dec": 5.492057016906403,
        "ra": 209.52823969727436,
        "sparcl_id": "000d4892-9931-11ee-9e4d-525400aad0aa",
    },
    {
        "_dr": "BOSS-DR16",
        "dec": 27.461703,
        "ra": 141.95067,
        "sparcl_id": "001b11a6-992f-11ee-993c-525400aad0aa",
    },
]

# OLD as of Dec 14, 2023
# find_4 = [
#    "0002f55c-75d7-11ee-822f-525400aad0aa",
#    "000df610-75d7-11ee-9957-525400aad0aa",
#    "0018f253-75d7-11ee-8253-525400aad0aa",
# ]

# OLD as of March 13, 2024
# find_4 = ['00063e73-992e-11ee-ad57-525400aad0aa',
#          '000d4892-9931-11ee-9e4d-525400aad0aa',
#          '000e388f-992d-11ee-a373-525400aad0aa']

find_4 = [
    "00063e73-992e-11ee-ad57-525400aad0aa",
    "000d4892-9931-11ee-9e4d-525400aad0aa",
    "001b11a6-992f-11ee-993c-525400aad0aa",
]

find_5a = [
    {"_dr": "BOSS-DR16", "data_release": "BOSS-DR16", "mjd": 55689},
    {"_dr": "SDSS-DR16", "data_release": "SDSS-DR16", "mjd": 54763},
]

find_5d = []

# OLD as of Dec 14, 2023
# reorder_1a = [
#    "9452379f-d82d-43bb-8fc2-c26451df4710",
#    "529936c6-14ef-4119-a80d-b184dcb6308e",
#    "fbb22144-25c5-4330-9b0b-8b2eac83079c",
# ]

# OLD as of March 13, 2024
# reorder_1a = ['00063e73-992e-11ee-ad57-525400aad0aa',
#              '000d4892-9931-11ee-9e4d-525400aad0aa',
#              '000e388f-992d-11ee-a373-525400aad0aa']

reorder_1a = [
    "00063e73-992e-11ee-ad57-525400aad0aa",
    "000d4892-9931-11ee-9e4d-525400aad0aa",
    "001b11a6-992f-11ee-993c-525400aad0aa",
]

# OLD as of Dec 14, 2023
# reorder_1b = [1254334738051655680, 1254335012929562624, 1254335287807469568]

# OLD as of March 13, 2024
# reorder_1b = [39627926995470031, 39627920993422590, 2258670445286942720]

reorder_1b = [39627926995470031, 39627920993422590, -5672180510041550848]

# OLD as of Dec 14, 2023
# reorder_2a = [1254334738051655680, 1254335012929562624, None]

reorder_2a = [
    "00063e73-992e-11ee-ad57-525400aad0aa",
    "000d4892-9931-11ee-9e4d-525400aad0aa",
    "None",
]

# OLD as of Dec 14, 2023
# reorder_2b = [1254334738051655680, 1254335012929562624, None]

reorder_2b = [39627926995470031, 39627920993422590, None]

authorized_1 = {
    "Loggedin_As": "test_user_1@noirlab.edu",
    "Authorized_Datasets": {
        "BOSS-DR16",
        "DESI-EDR",
        "SDSS-DR16",
        "SDSS-DR17-test",
    },
}

authorized_2 = {
    "Loggedin_As": "test_user_2@noirlab.edu",
    "Authorized_Datasets": {"BOSS-DR16", "DESI-EDR", "SDSS-DR16"},
}

authorized_3 = {
    "Loggedin_As": "Anonymous",
    "Authorized_Datasets": {"BOSS-DR16", "DESI-EDR", "SDSS-DR16"},
}

auth_find_1 = [
    ("84452fad-dbe7-11ee-a970-525400aad0aa", "SDSS-DR17-test"),
    ("847e0be4-dbe7-11ee-b095-525400aad0aa", "SDSS-DR17-test"),
]

auth_find_2 = [
    "00769ec9-9931-11ee-97de-525400aad0aa",
    "00b0904d-992f-11ee-b7f9-525400aad0aa",
    "00c6d798-9931-11ee-af11-525400aad0aa",
]

auth_find_4 = [
    "00769ec9-9931-11ee-97de-525400aad0aa",
    "00b0904d-992f-11ee-b7f9-525400aad0aa",
    "00c6d798-9931-11ee-af11-525400aad0aa",
    "010eb4d0-992f-11ee-89de-525400aad0aa",
    "014ac8ea-9931-11ee-b693-525400aad0aa",
    "01c9187a-9931-11ee-bbbc-525400aad0aa",
    "01db0ea0-9930-11ee-a576-525400aad0aa",
    "020ed77c-992f-11ee-aefb-525400aad0aa",
    "022ab30b-9931-11ee-a372-525400aad0aa",
    "024c9ba1-9930-11ee-aa56-525400aad0aa",
]

auth_find_6 = [
    "00769ec9-9931-11ee-97de-525400aad0aa",
    "00b0904d-992f-11ee-b7f9-525400aad0aa",
    "00c6d798-9931-11ee-af11-525400aad0aa",
    "010eb4d0-992f-11ee-89de-525400aad0aa",
    "014ac8ea-9931-11ee-b693-525400aad0aa",
    "01c9187a-9931-11ee-bbbc-525400aad0aa",
    "01db0ea0-9930-11ee-a576-525400aad0aa",
    "020ed77c-992f-11ee-aefb-525400aad0aa",
    "022ab30b-9931-11ee-a372-525400aad0aa",
    "024c9ba1-9930-11ee-aa56-525400aad0aa",
]

auth_retrieve_1 = (
    "SDSS-DR16, 3848 ; SDSS-DR16, 3848 ; "
    "SDSS-DR17-test, 3859 ; SDSS-DR17-test, 3859 ; "
)

auth_retrieve_2 = (
    "DESI-EDR, 7781 ; BOSS-DR16, 4615 ; "
    "BOSS-DR16, 4615 ; SDSS-DR16, 3848 ; "
    "SDSS-DR16, 3848 ; DESI-EDR, 7781 ; "
    "SDSS-DR17-test, 3859 ; SDSS-DR17-test, 3859 ; "
)

auth_retrieve_5 = "SDSS-DR16, 3848 ; SDSS-DR16, 3848 ; "

auth_retrieve_8 = "SDSS-DR16, 3848 ; SDSS-DR16, 3848 ; "
