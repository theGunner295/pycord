# This example requires the 'members' privileged intent to use the Member converter.

import pycord

intents = pycord.Intents.default()
intents.members = True

bot = pycord.Bot(
    debug_guilds=[...],
    description="An example to showcase how to extract info about users.",
    intents=intents,
)


@bot.slash_command(name="userinfo", description="Gets info about a user.")
async def info(ctx: pycord.ApplicationContext, user: pycord.Member = None):
    user = (
        user or ctx.author
    )  # If no user is provided it'll use the author of the message
    embed = pycord.Embed(
        fields=[
            pycord.EmbedField(name="ID", value=str(user.id), inline=False),  # User ID
            pycord.EmbedField(
                name="Created",
                value=pycord.utils.format_dt(user.created_at, "F"),
                inline=False,
            ),  # When the user's account was created
        ],
    )
    embed.set_author(name=user.name)
    embed.set_thumbnail(url=user.display_avatar.url)

    if user.colour.value:  # If user has a role with a color
        embed.colour = user.colour

    if isinstance(user, pycord.User):  # Checks if the user in the server
        embed.set_footer(text="This user is not in this server.")
    else:  # We end up here if the user is a discord.Member object
        embed.add_field(
            name="Joined",
            value=pycord.utils.format_dt(user.joined_at, "F"),
            inline=False,
        )  # When the user joined the server

    await ctx.respond(embeds=[embed])  # Sends the embed


bot.run("TOKEN")
