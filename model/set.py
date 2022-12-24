from model.model import Model


class SetModel(Model):
    def __init__(self, id, name, type, description, usage, link=None):
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.usage = usage
        self.link = link

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'name', 'type', 'description', 'usage']
        additional_keys = ['link']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init set: {key} is missing')

        kwargs = {key: values.get(key) for key in required_keys + additional_keys if key in values}
        return SetModel(**kwargs)
