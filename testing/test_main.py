import pytest
from main import get_none
from main import flatten_dict

def test_get_none():
    assert get_none() == None

class Test_flatten_dict:
    def test_simple_value(self):
        with pytest.raises(ValueError):
            flatten_dict(6)
            
    def test_no_dict_collection(self):
        with pytest.raises(ValueError):
            flatten_dict([6])

    def test_single_element_dict(self):
        assert flatten_dict({'key': 6}) == [6]

    def mult_element_dict(self):
        assert flatten_dict({'key1': 6, 'key2': True, 'key3': 'boom'}) == [6, True, 'boom']

    def empty_dict(self):
        assert flatten_dict({}) == []

    def complex_lists_one_deep(self):
        assert flatten_dict({'key1': 8, 'key2': {'key3': 4, 'key4': 5}}) == [8, 4, 5]

    def complex_lists_two_deep(self):
        assert flatten_dict({'key1': 8, 'key2': {'key3': {'key4': 4, 'key4': 5}}}) == [8, 4, 5]
