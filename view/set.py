from typing import List

from view.view import View
from model.set import SetModel


class SetsView(View):
    model: List[SetModel]

    def _source_string(self, source: str, sets: List[SetModel]):
        lines = [f'__**{source}**__:']
        lines.extend([f'\t**{set.name}**: {set.link}' for set in sets])
        return '\n'.join(lines)

    def string(self) -> str:
        data = {}

        for set in self.model:
            if set.source not in data:
                data[set.source] = []
            data[set.source].append(set)

        return "\n\n".join([self._source_string(source, sets) for source, sets in data.items()])
