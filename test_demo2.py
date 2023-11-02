import pytest as pytest


def test_thirdProgram():
    msg= "hello"
    assert msg == "hi","not matched"


#@pytest.mark.skip
@pytest.mark.xfail
def test_creditcardProgram():
    a=2
    b=4
    assert  a+3 == b,  "Right"



