import pytest
from bank import BankAccount

def setup_teardown():
    print("\nSetup: preparing test")
    yield
    print("Teardown: cleaning up after test")

def test_first_teardown(setup_teardown):
    print("Running first teardown test")
    assert True
    