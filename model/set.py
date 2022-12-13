from model.model import Model


class SetModel(Model):
    def __init__(self, id, name, type, description, usage):
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.usage = usage

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'type', 'description', 'usage']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init set: {key} is missing')

        args = tuple(values[key] for key in required_keys)
        return SetModel(*args)
