import pytest


def testLogin():
    print("Login Successful")


@pytest.mark.test
def testLogoff():
    print("Logout successful")


@pytest.mark.skip
def testCalculation():
    assert 2 + 2 == 4
