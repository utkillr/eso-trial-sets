from view.view import View
from model.boss import BossModel
from model.set_advice import SetAdviceModel


class BossView(View):
    model: BossModel

    def _set_advice_string(self, set_advice: SetAdviceModel) -> str:
        lines = []
        lines.append(f'\t**{set_advice.set.name}** ({set_advice.set.type})')

        if set_advice.set.description:
            lines.append(f'\t\t{set_advice.set.description}')

        if set_advice.set.link:
            lines.append(f'\t\t{set_advice.set.link}')

        if set_advice.why:
            lines.append(f'\t\t**Why?** *{set_advice.why}*')

        return '\n'.join(lines)
    
    def string(self) -> str:
        lines = [f'__**{self.model.name}**__']
        if self.model.description:
            lines.append(f'{self.model.description}')

        if self.model.links:
            lines.append('Links:')
            lines.extend([f'\t{link}' for link in self.model.links])

        no_set_lines = '\n\n'.join([self._set_advice_string(set) for set in self.model.tactic.no_sets])
        if no_set_lines:
            lines.append('')
            lines.append('Sets **NOT** to use:')
            lines.append(no_set_lines)

        set_lines = '\n\n'.join([self._set_advice_string(set) for set in self.model.tactic.sets])
        if set_lines:
            lines.append('')
            lines.append('Sets **TO USE**:')
            lines.append(set_lines)

        return '\n'.join(lines)
