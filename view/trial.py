from typing import List

from view.view import View
from model.trial import TrialModel
from model.boss import BossModel
from model.set_advice import SetAdviceModel


class TrialView(View):
    model: TrialModel

    def _set_advice_string(self, set_advice: SetAdviceModel) -> str:
        return f'\t\t**{set_advice.set.name}**: {set_advice.why}'

    def _boss_string(self, boss: BossModel) -> str:
        lines = [f'\t__**{boss.name}**__']

        no_set_lines = '\n'.join([self._set_advice_string(set) for set in boss.tactic.no_sets])
        if no_set_lines:
            lines.append('\tSets **NOT** to use:')
            lines.append(no_set_lines)

        set_lines = '\n'.join([self._set_advice_string(set) for set in boss.tactic.sets])
        if set_lines:
            lines.append('\tSets **TO USE**:')
            lines.append(set_lines)

        return '\n'.join(lines)

    def string(self) -> str:
        lines = [f'__**{self.model.name}**__']
        if self.model.description:
            lines.append(f'{self.model.description}')

        if self.model.links:
            lines.append('Links:')
            lines.extend([f'\t{link}' for link in self.model.links])

        boss_lines = '\n\n'.join([self._boss_string(boss) for boss in self.model.bosses])
        if boss_lines:
            lines.append('Bosses:')
            lines.append(boss_lines)

        return '\n'.join(lines)


class TrialsView(View):
    model: List[TrialModel]

    def _boss_string(self, boss: BossModel) -> str:
        return f'\t{boss.name}'

    def _trial_string(self, trial: TrialModel) -> str:
        lines = [f'__**{trial.name}**__']
        if trial.description:
            lines.append(f'{trial.description}')

        if trial.links:
            lines.append('Links:')
            lines.extend([f'\t{link}' for link in trial.links])

        bosses_line = '\n'.join([self._boss_string(boss) for boss in trial.bosses])
        if bosses_line:
            lines.append('Bosses:')
            lines.append(bosses_line)

        return '\n'.join(lines)

    def string(self) -> str:
        return "\n\n".join([self._trial_string(trial) for trial in self.model])
