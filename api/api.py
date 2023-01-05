import interactions

from config.config import Config
from orm.db import DataBase
from service.feedback import save_feedback
from service.suggest import save_suggest
from view.boss import BossView
from view.set import SetsView
from view.trial import TrialView, TrialsView
from view.adapter import ViewAdapter

bot = interactions.Client(Config.get().token)


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


def trial_option():
    return interactions.Option(
        name='trial',
        description='Name of the trial',
        type=interactions.OptionType.STRING,
        required=True,
        choices=[
            interactions.Choice(name=trial.name, value=trial.id)
            for trial in DataBase.get().get_trials_only()
        ]
    )


def boss_option():
    return interactions.Option(
        name='boss',
        description='Name of the boss',
        type=interactions.OptionType.STRING,
        required=True,
        autocomplete=True,
    )


def set_option():
    return interactions.Option(
        name='set',
        description='Name of the set',
        type=interactions.OptionType.STRING,
        required=True,
        autocomplete=True,
    )


@bot.command(
    name='sets-help',
    description='Help',
)
async def help(ctx: interactions.CommandContext):
    with open(Config.get().help_src) as f:
        await ctx.send(f.read())


@bot.command(
    name='sets-trials-all',
    description='List possible trials',
)
async def trials_all(ctx: interactions.CommandContext):
    try:
        db = DataBase.get()
        trials = db.get_trials_with_bosses()
        result = TrialsView(trials).string()
        for message in ViewAdapter(result).adapt():
            await ctx.send(message, suppress_embeds=True)
    except Exception as e:
        await ctx.send(f'Exception: {e}')


@bot.command(
    name='sets-trial',
    description='Describe working sets for each boss of the trial',
    options=[
        trial_option(),
        role_option(),
    ]
)
async def trial(ctx: interactions.CommandContext, trial: str, role: str):
    try:
        db = DataBase.get()
        trial_model = db.get_trial(trial, role)
        result = TrialView(trial_model).string()
        for message in ViewAdapter(result).adapt():
            await ctx.send(message, suppress_embeds=True)
    except Exception as e:
        await ctx.send(f'Exception: {e}')


@bot.command(
    name='sets-boss',
    description='Describe working sets for certain boss of the trial',
    options=[
        trial_option(),
        boss_option(),
        role_option(),
    ]
)
async def boss(ctx: interactions.CommandContext, trial: str, boss: str, role: str):
    try:
        db = DataBase.get()
        bosses = db.get_trial_bosses(trial)
        for boss_model in bosses:
            if boss_model.id == boss:
                boss_model = db.get_boss(boss, role)
                result = BossView(boss_model).string()
                for message in ViewAdapter(result).adapt():
                    await ctx.send(message, suppress_embeds=True)
                return
        else:
            raise ValueError(f'No boss {boss} in trial {trial}')
    except Exception as e:
        await ctx.send(f'Exception: {e}')


@bot.command(
    name='sets-list',
    description='List all of the available sets in bot',
)
async def sets(ctx: interactions.CommandContext):
    try:
        db = DataBase.get()
        sets = db.get_sets()
        result = SetsView(sets).string()
        for message in ViewAdapter(result).adapt():
            await ctx.send(message, suppress_embeds=True)
    except Exception as e:
        await ctx.send(f'Exception: {e}')


@bot.command(
    name='sets-feedback',
    description='Give some feedback in a freehand',
    options=[
        interactions.Option(
            name='message',
            description='Message of your feedback',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def feedback(ctx: interactions.CommandContext, message: str):
    try:
        save_feedback(ctx.user.username, message)
        await ctx.send('Your feedback sent!')
    except Exception as e:
        await ctx.send(f'Exception: {e}')


@bot.command(
    name='sets-suggest',
    description='Suggest your set for the boss',
    options=[
        trial_option(),
        role_option(),
        boss_option(),
        set_option(),
        interactions.Option(
            name='use',
            description='Should one use this set there?',
            type=interactions.OptionType.BOOLEAN,
            required=True,
            choices=[
                interactions.Choice(name='Yes', value=True),
                interactions.Choice(name='No', value=False),
            ]
        ),
        interactions.Option(
            name='why',
            description='Why is this set useful there?',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def suggest(ctx: interactions.CommandContext, trial: str, role: str, boss: str, set: str, use: bool, why: str):
    try:
        db = DataBase.get()
        bosses = db.get_trial_bosses(trial)
        for boss_model in bosses:
            if boss_model.id == boss:
                save_suggest(ctx.user.username, trial, boss, role, set, use, why)
                return await ctx.send('Your suggestion sent!')
        else:
            raise ValueError(f'No boss {boss} in trial {trial}')
    except Exception as e:
        await ctx.send(f'Exception: {e}')


"""
AUTOCOMPLETE
"""


async def autocomplete_boss(ctx, user_input: str = ''):
    options = ctx.data.options
    trial_option = next((option for option in options if option.name == 'trial'), None)
    if not trial_option:
        return await ctx.populate([])

    bosses = DataBase.get().get_trial_bosses(trial_id=trial_option.value)
    if not bosses:
        return await ctx.populate([])

    await ctx.populate(
        [
            interactions.Choice(name=boss.name, value=boss.id)
            for boss in bosses
            if user_input.lower() in boss.name
        ]
    )


async def autocomplete_set(ctx, user_input: str = ''):
    sets = DataBase.get().get_sets()
    substring = user_input.lower()

    await ctx.populate(
        [
            interactions.Choice(name=set.name, value=set.id)
            for set in sets
            if substring in set.name.lower() or substring in set.id.lower()
        ][:10]
    )


@bot.autocomplete(command='sets-boss', name='boss')
async def autocomplete_boss_boss(ctx, user_input: str = ''):
    return await autocomplete_boss(ctx, user_input)


@bot.autocomplete(command='sets-suggest', name='boss')
async def autocomplete_suggest_boss(ctx, user_input: str = ''):
    return await autocomplete_boss(ctx, user_input)


@bot.autocomplete(command='sets-suggest', name='set')
async def autocomplete_suggest_set(ctx, user_input: str = ''):
    return await autocomplete_set(ctx, user_input)
