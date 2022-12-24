from model.model import Model


class BossModel(Model):

    def __init__(self, id, name, description, links=None, tactic=None):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.links = links if links else []
        self.tactic = tactic

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'description']
        additional_keys = ['tactic', 'links']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init boss: {key} is missing')

        kwargs = {key: values.get(key) for key in required_keys + additional_keys if key in values}
        return BossModel(**kwargs)
