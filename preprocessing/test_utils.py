"""Test utils"""

import pytest
from utils import _hla_length_filter


def test_hla_length_filter():
    assert _hla_length_filter("A*5:27:08") == "A*5:27"
    assert _hla_length_filter("A*5:27") == "A*5:27"


def test_hla_length_filter_exc():
    with pytest.raises(ValueError):
        _hla_length_filter("A:*527")
