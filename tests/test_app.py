import pytest
from app import soma, media

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_media():
    assert media([2, 4, 6]) == 4

def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])
