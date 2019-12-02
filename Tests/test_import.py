import pytest
from os import listdir
from os.path import isfile, join

def test_back():
    path = 'Sprites/back/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    assert len(files) == 152

def test_front():
    path = 'Sprites/front/'
    files = [f for f in listdir(path) if isfile(join(path, f))]
    assert len(files) == 152