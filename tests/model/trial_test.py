import pytest

from model.trial import TrialModel


def _default_data():
    return {
        'id': 'test-id',
        'name': 'test-name',
        'description': 'test-description',
    }


def _default_test(set: TrialModel):
    assert set.id == 'test-id'
    assert set.name == 'test-name'
    assert set.description == 'test-description'


def test_trial_model_min():
    data = _default_data()
    trial = TrialModel.from_dict(data)
    _default_test(trial)
    assert trial.bosses is None
    assert len(trial.links) == 0


def test_trial_model_max():
    data = _default_data()
    links = ['1', '2', '3']
    bosses = ['a', 'b', 'c']
    data['links'] = links
    data['bosses'] = bosses
    trial = TrialModel.from_dict(data)
    _default_test(trial)
    assert trial.links == links
    assert trial.bosses == bosses


def test_trial_model_miss():
    data = _default_data()
    del data['id']
    with pytest.raises(ValueError):
        TrialModel.from_dict(data)


def test_set_model_extra():
    data = _default_data()
    data['eh'] = 'eh'
    trial = TrialModel.from_dict(data)
    _default_test(trial)
