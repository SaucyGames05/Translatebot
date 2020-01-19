import discord
from discord.ext import commands
import asyncio
from googletrans import Translator

client = commands.Bot(command_prefix = "~")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Google Dino Game'))
    print("TranslateBot is ready")

@client.command(aliases=['trans'])
async def _trans(ctx):
    translates = ctx.message.content[6:]
    translator = Translator()
    output = translator.translate(translates, dest="en")
    await ctx.send(f'>>> Translation: `"{output.text}"`\nTranslated from: `{output.src}`\nPronunciation: `"{output.pronunciation}"`', tts=True)

@client.command(aliases=['translate'])
async def _trans2(ctx):
    translates = ctx.message.content[10:]
    translator = Translator()
    output = translator.translate(translates, dest="en")
    await ctx.send(f'>>> Translation: `"{output.text}"`\nTranslated from: `{output.src}`\nPronunciation: `"{output.pronunciation}"`', tts=True)

@client.command(aliases=['tts'])
async def _tts(ctx):
  await ctx.send("> To turn off Text-to-Speech, go to `TranslateBot` role and turn off `Send TTS Messages` setting.")

@client.command(aliases=['about'])
async def _about(ctx):
  await ctx.send("Hi! I'm TranslateBot! I use Google Translate to take your inputs and translate them into english. I work just like google translate, but in your discord server!")

@client.command(aliases=['sendhelp'])
async def _help1(ctx):
  await ctx.send(">>> Commands:\n`~sendhelp` ***Get help!***\n`~about` ***Learn more about me!***\n`~trans [INPUT]` or `~translate [INPUT]` ***Translate anything to English!***\n`~tts` ***Learn how to turn off TTS!***")

client.run("BOT_TOKEN")
