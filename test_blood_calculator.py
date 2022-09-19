import pytest 

@pytest.mark.parametrize("input_age, expected", 
    [(85, "Normal"),
    (50, "Borderline Low"),
    (30, "Low")
    ]
)




def test_check_HDL(input_age, expected): 
    from blood_calculator import check_HDL
    answer = check_HDL(input_age)
    
    assert answer == expected 
    
