import pytest
import findstring
import importlib

def test_ispresent():
    assert findstring.ispresent("Al")

def test_nodigit():
    assert findstring.nodigit('Al')
