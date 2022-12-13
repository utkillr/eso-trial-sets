from model.model import Model


class BossModel(Model):

    def __init__(self, id, name, description, tactic=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.tactic = tactic

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'description']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init boss: {key} is missing')

        args = tuple(values[key] for key in required_keys)
        return BossModel(*args)
