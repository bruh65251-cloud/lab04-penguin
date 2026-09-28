
def setup_teardown():
    print("\nSetup: preparing test")
    yield
    print("Teardown: cleaning up after test")


def test_first_teardown(setup_teardown):
    print("Running first teardown test")
    assert True


def test_second_teardown(setup_teardown):
    print("Running second teardown test")
    assert True