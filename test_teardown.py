import pytest


@pytest.fixture
def setup_teardown():
    print("[setup]")
    yield
    print("[teardown]")


def test_first_teardown(setup_teardown):
    print("Running first teardown test")
    assert True


def test_second_teardown(setup_teardown):
    print("Running second teardown test")
    assert True