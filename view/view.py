from typing import List, Union

from model.model import Model


class View:

    model: Model

    def __init__(self, model: Union[Model, List[Model]]):
        self.model = model

    def string(self) -> str:
        pass
