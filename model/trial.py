from model.model import Model


class TrialModel(Model):
    def __init__(self, id, name, description, links=None, bosses=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.links = links if links else []
        self.bosses = bosses

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'description']
        additional_keys = ['links', 'bosses']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init trial: {key} is missing')

        kwargs = {key: values.get(key) for key in required_keys + additional_keys if key in values}
        return TrialModel(**kwargs)
