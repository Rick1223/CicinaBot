

import discord
from discord import app_commands
from discord.ext import commands
import random
import os
from datetime import timedelta

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot je online: {bot.user}")


@bot.tree.command(name="cicina", description="Cicina Checker 😂")
@app_commands.guild_only()
async def cicina(interaction: discord.Interaction):

    member = interaction.user
    cm = random.randint(1, 35)

    if cm < 5:
        try:
            await member.timeout(
                timedelta(hours=1),
                reason="Cicina Checker: menej ako 5 cm"
            )

            await interaction.response.send_message(
                f"💀 CICINA CHECKER 💀\n"
                f"Výsledok: {cm} cm\n"
                f"Neúspešný checker! Timeout na 1 hodinu 😂"
            )

        except discord.Forbidden:
            await interaction.response.send_message(
                "Nemám právo udeliť timeout!",
                ephemeral=True
            )

    else:
        await interaction.response.send_message(
            f"🟢 CICINA CHECKER\n"
            f"Výsledok: {cm} cm\n"
            f"Prešiel si checkerom! 😂"
        )


if not TOKEN:
    raise RuntimeError("Chýba TOKEN v nastaveniach hostingu!")

bot.run(TOKEN)
