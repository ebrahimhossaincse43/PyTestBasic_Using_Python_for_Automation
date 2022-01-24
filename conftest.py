import pytest


@pytest.fixture(autouse= True)
def setUp():
    print("launch browser")
    print("log in")
    print("browse product")
    yield
    print("logout")
    print("close")