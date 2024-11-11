import pytest


@pytest.fixture(autouse=True)
def deleter():
    with open('testfile_15415.txt', 'w'):
        pass