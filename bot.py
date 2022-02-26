import discord
import json
import generator
import random
import asyncio

key = ""

with open("key.txt", "r") as f:
    key = f.read().strip()

generating = False

client = discord.Client()


def generate_maps():
    global generating
    print("regenerating maps")
    generating = True
    generator.generate_average_map()
    generator.generate_starrable_map()
    print("regenerated maps")
    generating = False


generate_maps()


@client.event
async def on_ready():
    customActivity = discord.Game("thinking about strange things")
    await client.change_presence(status=discord.Status.online, activity=customActivity)

    print("The bot is ready")


@client.event
async def on_message(message):
    global generating

    if message.author == client.user:
        return

    if message.content.strip() == "??regen" and message.author.id == 384499090865782785:
        await message.channel.send(
            "Regenerating Maps!", allowed_mentions=discord.AllowedMentions.none()
        )
        generate_maps()
        await message.channel.send(
            "Regenerated Maps!", allowed_mentions=discord.AllowedMentions.none()
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
