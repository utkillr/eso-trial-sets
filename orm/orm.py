import json
from typing import List


class DAL:
    model = ''
    base = 'src'
    file = ''

    def __init__(self):
        self.src = f'{self.base}/{self.file}'
        with open(self.src) as f:
            self.data = json.loads(f.read())

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