import interactions

from orm.db import DataBase
from view.trial import TrialView, TrialsView
from view.boss import BossView

bot = interactions.Client('MTA0NjM2MDE3NDA3MzQ4MzMzNA.GuNFxE.e0joIH9MxvuB6Rod4VwHpD5GZFDkmN7pdUBKDk')


def role_option():
    return interactions.Option(
        name='role',
        description='Interesting role',
        type=interactions.OptionType.STRING,
        required=True,
        choices=[
            interactions.Choice(name='DD', value='dd'),
            interactions.Choice(name='Tank', value='tank'),
            interactions.Choice(name='Healer', value='heal'),
        ]
    )


@bot.command(
    name='list-trials',
    description='List possible trials',
)
async def list_trials(ctx: interactions.CommandContext):
    db = DataBase()
    trials = db.get_trials_with_bosses()
    await ctx.send(TrialsView(trials).string())


@bot.command(
    name='trial-sets',
    description='Describe working sets for each boss of the trial',
    options=[
        interactions.Option(
            name='trial',
            description='Name of the trial',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name=trial.name, value=trial.id)
                for trial in DataBase().get_trials_only()
            ]
        ),
        role_option(),
    ]
)
async def trial_sets(ctx: interactions.CommandContext, trial: str, role: str):
    db = DataBase()
    trial_model = db.get_trial(trial, role)
    await ctx.send(TrialView(trial_model).string())


@bot.command(
    name='boss-sets',
    description='Describe working sets for certain boss of the trial',
    options=[
        interactions.Option(
            name='trial',
            description='Name of the trial',
            type=interactions.OptionType.STRING,
            required=True,
            choices=[
                interactions.Choice(name=trial.name, value=trial.id)
                for trial in DataBase().get_trials_only()
            ]
        ),
        interactions.Option(
            name='boss',
            description='Name of the boss',
            type=interactions.OptionType.STRING,
            required=True,
            autocomplete=True,
        ),
        role_option(),
    ]
)
async def boss_sets(ctx: interactions.CommandContext, trial: str, boss: str, role):
    db = DataBase()
    bosses = db.get_trial_bosses(trial)
    for boss_model in bosses:
        if boss_model.id == boss:
            boss_model = db.get_boss(boss, role)
            return await ctx.send(BossView(boss_model).string())
    raise ValueError(f'No boss {boss} in trial {trial}')


"""
AUTOCOMPLETE
"""

@bot.autocomplete(command='boss-sets', name='boss')
async def autocomplete_boss_sets_boss(ctx, user_input: str = ''):
    options = ctx.data.options
    trial_option = next((option for option in options if option.name == 'trial'), None)
    if not trial_option:
        return await ctx.populate([])

    bosses = DataBase().get_trial_bosses(trial_id=trial_option.value)
    if not bosses:
        return await ctx.populate([])

    await ctx.populate(
        [
            interactions.Choice(name=boss.name, value=boss.id)
            for boss in bosses
            if user_input.lower() in boss.name
        ]
    )
