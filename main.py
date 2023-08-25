import discord
import pyttsx3
from discord.ext import commands

golos = pyttsx3.init()
bot = commands.Bot(command_prefix="~", intents=discord.Intents.all())


@bot.event
async def on_ready():
    print("Бот в сети")


@bot.command()
async def author(ctx):
    await ctx.send(f"Мой создатель: Телков Антон#8518")


@bot.command()
async def run(ctx, rate=150):
    if 0 < int(rate) < 1000:
        golos.setProperty("rate", int(rate))
    else:
        golos.setProperty("rate", 150)
    print(rate)
    golos.setProperty("valume", 10)
    if ctx.message.author.voice:
        vs = await ctx.message.author.voice.channel.connect()
        vs.play(discord.FFmpegPCMAudio("444.mp3"))


@bot.command()
async def stop(ctx):
    if ctx.message.author.voice:
        discord.utils.get(bot.voice_clients, guild=ctx.guild).stop()
        await discord.utils.get(bot.voice_clients, guild=ctx.guild).disconnect()


@bot.command()
async def sk(ctx, *content):
    content = " ".join(content)
    golos.say(content)
    golos.save_to_file(content, "1.mp3")
    golos.runAndWait()
    discord.utils.get(bot.voice_clients, guild=ctx.guild) \
        .play(discord.FFmpegPCMAudio("1.mp3"))


@bot.event
async def on_message(message):
    print(message.content)
    if message.author == bot.user:
        return

    if "~" not in message.content:
        print(message.content)
        message.content = "~sk " + message.content
        print(message.content)

    await bot.process_commands(message)


bot.run("MTA5ODU1NzgwNjM4NDI1NTAwNg.GJDnWB.9BJf114iYg30lpFjf9M7kDY0eSYs1vU7hZmydA")
