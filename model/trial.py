from model.model import Model


class TrialModel(Model):
    def __init__(self, id, name, description, bosses=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.bosses = bosses

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'description']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init trial: {key} is missing')

        args = tuple(values[key] for key in required_keys)
        return TrialModel(*args)
