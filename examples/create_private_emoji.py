import pycord

bot = pycord.Bot()

allowed_content_types = [
    "image/jpeg",
    "image/png",
]  # Setting up allowed attachments types


# Discord doesn't support creating private emojis by default, its semi-implemented feature and can be done by bots only.

# This command is publicly available, to set up command permissions look for other examples in repo
@bot.command(guild_ids=[...])
async def add_private_emoji(
    ctx,
    name: pycord.Option(str),
    image: pycord.Option(pycord.Attachment),
    role: pycord.Option(pycord.Role),
):
    if image.content_type not in allowed_content_types:
        return await ctx.respond("Invalid attachment type!", ephemeral=True)

    image_file = await image.read()  # Reading attachment's content to get bytes

    await ctx.guild.create_custom_emoji(
        name=name, image=image_file, roles=[role]
    )  # Image argument only takes bytes!
    await ctx.respond(content="Private emoji is successfully created!")


bot.run("TOKEN")
