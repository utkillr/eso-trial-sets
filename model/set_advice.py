from model.model import Model


class SetAdviceModel(Model):
    def __init__(self, id, why, set=None):
        super().__init__()
        self.id = id
        self.why = why
        self.set = set

    @classmethod
    def from_dict(cls, values):
        required_keys = ['id', 'why']
        for key in required_keys:
            if key not in values:
                raise ValueError(f'Unable to init set advice: {key} is missing')

        args = tuple(values[key] for key in required_keys)
        return SetAdviceModel(*args)
