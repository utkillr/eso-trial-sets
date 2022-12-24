import pytest

from model.set import SetModel


def _default_data():
    return {
        'id': 'test-id',
        'name': 'test-name',
        'type': 'test-type',
        'description': 'test-description',
        'usage': 'test-usage',
    }


def _default_test(set: SetModel):
    assert set.id == 'test-id'
    assert set.name == 'test-name'
    assert set.type == 'test-type'
    assert set.description == 'test-description'
    assert set.usage == 'test-usage'


def test_set_model_min():
    data = _default_data()
    set = SetModel.from_dict(data)
    _default_test(set)
    assert set.link is None


def test_set_model_max():
    data = _default_data()
    data['link'] = 'test-link'
    set = SetModel.from_dict(data)
    _default_test(set)
    assert set.link == 'test-link'


def test_set_model_miss():
    data = _default_data()
    del data['id']
    with pytest.raises(ValueError):
        SetModel.from_dict(data)


def test_set_model_extra():
    data = _default_data()
    data['eh'] = 'eh'
    set = SetModel.from_dict(data)
    _default_test(set)
