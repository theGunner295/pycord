import pycord

# Role selects (dropdowns) are a new type of select menu/dropdown Discord has added so people can select server roles from a dropdown.

# Defines a simple View that allows the user to use the Select menu.
# In this view, we define the role_select with `discord.ui.role_select`
# Using the decorator automatically sets `select_type` to `discord.ComponentType.role_select`.
class DropdownView(pycord.ui.View):
    @pycord.ui.role_select(
        placeholder="Select roles...", min_values=1, max_values=3
    )  # Users can select a maximum of 3 roles in the dropdown
    async def role_select_dropdown(
        self, select: pycord.ui.Select, interaction: pycord.Interaction
    ) -> None:
        await interaction.response.send_message(
            f"You selected the following roles:"
            + f", ".join(f"{role.mention}" for role in select.values)
        )


bot: pycord.Bot = pycord.Bot(debug_guilds=[...])


@bot.slash_command()
async def role_select(ctx: pycord.ApplicationContext) -> None:
    """Sends a message with our dropdown that contains a role select."""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our View
    await ctx.respond("Select roles:", view=view)


@bot.event
async def on_ready() -> None:
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


bot.run("TOKEN")
