import pytest


@pytest.mark.parametrize("inputHDL, expected",
                         [(85, "Normal"),
                          (50, "Borderline Low"),
                          (30, "Low")
                          ]
                         )
def test_check_HDL(inputHDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(inputHDL)

    assert answer == expected


@pytest.mark.parametrize("inputLDL, expected",
                         [(100, "Normal"),
                          (140, "Borderline high"),
                          (170, "High"),
                          (200, "Very high")
                          ]
                         )
def test_check_LDL(inputLDL, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(inputLDL)

    assert answer == expected


@pytest.mark.parametrize("inputCholesterol, expected",
                         [(190, "Normal"),
                          (220, "Borderline high"),
                          (250, "High")
                          ]
                         )
def test_check_total_cholesterol(inputCholesterol, expected):
    from blood_calculator import check_total_cholesterol
    answer = check_total_cholesterol(inputCholesterol)

    assert answer == expected
