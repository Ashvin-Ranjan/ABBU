import discord
import json
import generator
import random
import asyncio

key = ""

with open("key.txt", "r") as f:
    key = f.read().strip()

learn_messages = False
learn_starred = True
learn_afk = True

messages = []
starred = []
afk = []

with open("messages.json", "r") as f:
    messages = json.loads(f.read())

with open("starred.json", "r") as f:
    starred = json.loads(f.read())

with open("afk.json", "r") as f:
    afk = json.loads(f.read())

generating = False

client = discord.Client()


def generate_maps(init=False):
    global generating
    print("regenerating maps")
    generating = True
    if learn_messages or init:
        generator.generate_average_map()
    if learn_starred or init:
        generator.generate_starrable_map()
    if learn_afk or init:
        generator.generate_afk_map()
    print("regenerated maps")
    generating = False


generate_maps(True)


@client.event
async def on_ready():
    customActivity = discord.Game("thinking about strange things")
    await client.change_presence(status=discord.Status.online, activity=customActivity)

    print("The bot is ready")


@client.event
async def on_message(message):
    global generating, learn_messages, learn_starred

    if message.author == client.user:
        return

    if client.user in message.mentions:
        await message.channel.send(
            f"`Average Because Bread User` is AFK: {generator.generate_afk_message()}",
            allowed_mentions=discord.AllowedMentions.none(),
        )

    if message.content.strip() == "??regen" and message.author.id == 384499090865782785:
        await message.channel.send(
            "Regenerating Maps!", allowed_mentions=discord.AllowedMentions.none()
        )
        generate_maps()
        await message.channel.send(
            "Regenerated Maps!", allowed_mentions=discord.AllowedMentions.none()
        )
        return

    if (
        " I set your AFK: " in message.content
        and message.author.id == 155149108183695360
    ):
        afk.append(
            " I set your AFK: ".join(message.content.split(" I set your AFK: ")[1:])
            .replace(generator.START, "")
            .replace(generator.END, "")
            .strip()
        )
        with open("afk.json", "w") as f:
            f.write(json.dumps(afk))

    if (
        message.content.strip().startswith("??togglelearn")
        and len(message.content.strip().split(" ")) == 2
        and message.author.id == 384499090865782785
    ):
        if message.content.strip().split(" ")[1] == "starred":
            learn_starred = not learn_starred
            await message.channel.send(
                f"Will{' not' if not learn_starred else ''} learn starred messages"
            )

        if message.content.strip().split(" ")[1] == "messages":
            learn_messages = not learn_messages
            await message.channel.send(
                f"Will{' not' if not learn_messages else ''} learn general messages"
            )

        if message.content.strip().split(" ")[1] == "afk":
            learn_afk = not learn_afk
            await message.channel.send(
                f"Will{' not' if not learn_messages else ''} learn afk messages"
            )
        return

    if message.content.strip() == "??gsm":
        async with message.channel.typing():
            await asyncio.sleep(random.random())
            await message.channel.send(
                generator.generate_starrable_message()
                if not generating
                else "Please try again later, regenerating maps currently.",
                allowed_mentions=discord.AllowedMentions.none(),
            )

        return

    if message.content.strip() == "??ggm":
        async with message.channel.typing():
            await asyncio.sleep(random.random())
            await message.channel.send(
                generator.generate_average_message()
                if not generating
                else "Please try again later, regenerating maps currently.",
                allowed_mentions=discord.AllowedMentions.none(),
            )

        return

    if learn_messages and message.channel.id == 711821089746976768:
        messages.append(
            message.content.replace(generator.START, "").replace(generator.END, "")
        )
        with open("messages.json", "w") as f:
            f.write(json.dumps(messages))

    if (
        learn_starred
        and message.channel.id == 790677423083356182
        and len(message.embeds) == 1
        and message.embeds[0].title != "Average Because Bread User"
    ):
        starred.append(
            message.embeds[0]
            .description.replace(generator.START, "")
            .replace(generator.END, "")
        )
        with open("starred.json", "w") as f:
            f.write(json.dumps(starred))


client.run(key)
