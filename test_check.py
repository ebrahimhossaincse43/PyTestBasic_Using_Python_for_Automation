import pytest


def testRightCalculation():
    assert 2 + 2 == 4


@pytest.mark.test
def testWrongCalculation():
    assert 2 + 3 == 5
