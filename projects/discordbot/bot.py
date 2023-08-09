import os, random
import discord
from discord.ext import commands
from models import init_db, PythonQuestion

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
init_db()

@bot.command(name='quiz')
async def get_question(ctx):
    question = random.randint(1,6)
    question_obj = PythonQuestion.from_database(question)
    if question_obj:
        await ctx.send(str(question_obj))
    else:
        await ctx.send("Question not found")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

if __name__ == '__main__':
    bot.run(os.environ['DISCORD_TOKEN'])