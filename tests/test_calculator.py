from cicd_workshop.calculator import add, multiply

def test_add_should_return_sum():
    assert add(2, 3) == 5

def test_multiply_should_allow_negative_numbers():
    assert multiply(-2, 3) == -6
