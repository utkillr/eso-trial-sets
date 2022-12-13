import json
from typing import List


class DAL:
    model = ''
    src = []

    def __init__(self):
        self.data = {}
        for file in self.src:
            with open(file) as f:
                self.data.update(json.loads(f.read()))

    def get(self, obj_id: str) -> dict:
        if obj_id not in self.data:
            raise Exception(f'No {self.model} with id {obj_id}')
        return {'id': obj_id, **self.data.get(obj_id)}

    def get_all(self) -> List[dict]:
        return [
            {
                'id': key,
                **value
            } for key, value in self.data.items()
        ]