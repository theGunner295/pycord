import datetime

import pycord

bot = pycord.Bot(debug_guilds=[...])


@bot.slash_command()
async def timeout(
    ctx: pycord.ApplicationContext, member: pycord.Member, minutes: int
):
    """Apply a timeout to a member."""

    duration = datetime.timedelta(minutes=minutes)
    await member.timeout_for(duration)
    await ctx.respond(f"Member timed out for {minutes} minutes.")

    """
    The method used above is a shortcut for:

    until = discord.utils.utcnow() + datetime.timedelta(minutes=minutes)
    await member.timeout(until)
    """


bot.run("TOKEN")
