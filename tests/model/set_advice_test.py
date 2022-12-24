import pytest

from model.set_advice import SetAdviceModel


def _default_data():
    return {
        'id': 'test-id',
        'why': 'test-why',
    }


def _default_test(set_advice: SetAdviceModel):
    assert set_advice.id == 'test-id'
    assert set_advice.why == 'test-why'


def test_set_advice_model_min():
    data = _default_data()
    set_advice = SetAdviceModel.from_dict(data)
    _default_test(set_advice)
    assert set_advice.set is None


def test_set_advice_model_max():
    data = _default_data()
    data['set'] = 'set'
    set_advice = SetAdviceModel.from_dict(data)
    _default_test(set_advice)
    assert set_advice.set == 'set'


def test_set_advice_model_miss():
    data = _default_data()
    del data['id']
    with pytest.raises(ValueError):
        SetAdviceModel.from_dict(data)


def test_set_advice_model_extra():
    data = _default_data()
    data['eh'] = 'eh'
    set_advice = SetAdviceModel.from_dict(data)
    _default_test(set_advice)
