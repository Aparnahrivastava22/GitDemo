import pytest


def test_firstProgram(setup):
    print("Hello")


@pytest.mark.smoke
def test_secondProgram():
    print("bye")

#parametrizing///////
def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])