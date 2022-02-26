import discord
import json
import generator
import random
import asyncio

key = ""

with open("key.txt", "r") as f:
    key = f.read().strip()

generating = False


def generate_maps():
    global generating
    generating = True
    generator.generate_average_map()
    generator.generate_starrable_map()
    generating = False


generate_maps()


@client.event
async def on_ready():
    customActivity = discord.Game("thinking about strange things")
    await client.change_presence(status=discord.Status.online, activity=customActivity)

    update_emotes()

    print("The bot is ready")


@client.event
async def on_message(message):
    global generating
    update_emotes()

    if message.author == client.user or message.channel in ignore:
        return

    if message.content.strip() == "??regen" and message.author.id == 384499090865782785:
        generate_maps()

        return

    if message.content.strip() == "??gsm":
        async with message.channel.typing():
            await asyncio.sleep(random.random())
            await message.channel.send(generator.generate_starrable_message())

        return

    if message.content.strip() == "??ggm":
        async with message.channel.typing():
            await asyncio.sleep(random.random())
            await message.channel.send(generator.generate_average_message())

        return

    # learning
    # if learnnew:
    #     processed = message.content

    #     for i in dictionary_inv.keys():
    #         processed = processed.replace(i, "")

    #     for i in dictionary.keys():
    #         processed = processed.replace(i, dictionary[i])

    #     end = ""
    #     for char in processed:
    #         if (
    #             char in emoji.UNICODE_EMOJI
    #             or char in dictionary_inv.keys()
    #             or char == "\n"
    #             or char in specialcases
    #         ):
    #             end += char

    #     # learning and writing, and maybe reacting
    #     end = end.replace("\n", "n")
    #     if end.replace("n", "") != "" and (
    #         not message.author.bot or message.author.id in bots_allowed
    #     ):
    #         end = ":%s," % (end.strip("n"))
    #         with open("messages.txt", "a", encoding="utf-8") as f:
    #             f.write(end + "\n")
    #         print(message.content)
    #         print(end)


client.run(key)
