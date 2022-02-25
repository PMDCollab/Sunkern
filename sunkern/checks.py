from discord.ext import commands


def _is_admin_impl():  # todo args
    pass  # todo also check administrate permission!


def is_user():
    async def predicate(ctx):
        return False  # todo - also or _is_admin_impl
    return commands.check(predicate)


def is_admin():
    async def predicate(ctx):
        return False  # todo - _is_admin_impl
    return commands.check(predicate)

