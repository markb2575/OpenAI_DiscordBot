import lightbulb
import hikari
import openai

openai.api_key = "openai api_key goes here"

class PrivateChannel(object):
    def __init__(self, ctx, channel, starting):
        self.ctx = ctx
        self.channel = channel
        self.starting = starting
    
list = []

bot = lightbulb.BotApp(token="bot token goes here", intents=hikari.Intents.ALL)

@bot.command
@lightbulb.option("description", "The description given to the AI")
@lightbulb.command("imagine", "give the AI a description", auto_defer=1)
@lightbulb.implements(lightbulb.SlashCommand)
async def ask(ctx: lightbulb.Context) -> None:
    message = generateImage(ctx.options.description)
    try:      
        await ctx.respond(message)
    except:
        await ctx.respond("Could not generate a response.")

def generateImage(prompt):
    response = openai.Image.create(prompt=prompt, n=1, size="1024x1024")
    return response['data'][0]['url']

@bot.command
@lightbulb.option("prompt", "The prompt given to the AI")
@lightbulb.command("ask", "give the AI a prompt", auto_defer=1)
@lightbulb.implements(lightbulb.SlashCommand)
async def ask(ctx: lightbulb.Context) -> None:
    message = generateResponse(ctx.options.prompt)
    try:      
        await ctx.respond(message)
    except:
        await ctx.respond("Could not generate a response.")

def generateResponse(prompt):
    response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=.7, max_tokens=50)
    return response.choices[0].text

bot.run()