import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

@pytest.mark.xfail
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"


