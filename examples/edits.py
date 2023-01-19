import asyncio

import pycord

intents = pycord.Intents.default()
intents.message_content = (
    True  # < This may give you `read-only` warning, just ignore it.
)
# This intent requires "Message Content Intent" to be enabled at https://discord.com/developers


bot = pycord.Bot(intents=intents)


@bot.event
async def on_ready():
    print("Ready!")


@bot.event
async def on_message(message: pycord.Message):
    if message.content.startswith("!editme"):
        msg = await message.channel.send("10")
        await asyncio.sleep(3.0)
        await msg.edit(content="40")


@bot.event
async def on_message_edit(before: pycord.Message, after: pycord.Message):
    msg = (
        f"**{before.author}** edited their message:\n{before.content} ->"
        f" {after.content}"
    )
    await before.channel.send(msg)


bot.run("TOKEN")
