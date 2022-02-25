from typing import Union

from discord import Role, Message
from discord.ext import commands
from discord.ext.commands import Context, CommandError, guild_only

from sunkern.checks import is_admin, is_user
from sunkern.config.providers import ProviderPool

bot = commands.Bot(command_prefix='§',
                   description="A Discord bot for creating issues on Github and other platforms: "
                               "https://sunkern.pmdcollab.org")


@bot.command(description="Set the role that is allowed to use the §issue command.")
@guild_only()
@is_admin()
async def userrole(ctx: Context, role_to_set: Role):
    pass


@userrole.error
async def userrole_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command(description="Set the role that is allowed to use all commands.")
@guild_only()
@is_admin()
async def adminrole(ctx: Context, role_to_set: Role):
    pass


@adminrole.error
async def adminrole_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command()  # todo: description
@guild_only()
@is_user()
async def issue(ctx: Context, project_repo: str, title: str, description_or_message: Union[Message, str]):
    pass


@issue.error
async def issue_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command(description=f"Add a new project with the given name and provider (see §providers for list) "
                         f"and project ID.")
@guild_only()
@is_admin()
async def projectadd(ctx: Context, name: str, provider: str, project_id: str):
    pass


@project.error
async def projectadd_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command(description="Remove a previously registered project.")
@guild_only()
@is_admin()
async def projectdel(ctx: Context, name: str):
    pass


@projectdel.error
async def projectdel_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command(description="Set the default project. When not specifying a project in §issue, this one is used.")
@guild_only()
@is_admin()
async def projectdefault(ctx: Context, name: str):
    pass


@projectdefault.error
async def projectdefault_error(ctx: Context, error: CommandError):
    pass  # todo


@bot.command(description="Lists all available providers.")
@guild_only()
@is_admin()
async def providers(ctx: Context):
    for name, provider in ProviderPool.lst().items():
        pass  # todo
