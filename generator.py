import json
import random

START = "\ufffc"
END = "\ufffd"
AVERAGE_CONTEXT = 6
STARRABLE_CONTEXT = 6
AFK_CONTEXT = 4
average_values = {}
starrable_values = {}
afk_values = {}


def generate_average_map():
    messages = []

    with open("./messages.json") as f:
        messages = json.loads(f.read())
        messages = [o.replace(START, "").replace(END, "") for o in messages if o != ""]

    average_values[START] = []

    for i in messages:
        key = START
        average_values[key].append(i[0])
        for j in range(len(i)):
            key += i[j]
            key = key[-AVERAGE_CONTEXT:]
            toadd = END
            try:
                toadd = i[j + 1]
            except:
                pass
            if key not in average_values:
                average_values[key] = [toadd]
                continue

            average_values[key].append(toadd)


def generate_starrable_map():
    messages = []

    with open("./starred.json") as f:
        messages = json.loads(f.read())
        messages = [o.replace(START, "").replace(END, "") for o in messages if o != ""]

    starrable_values[START] = []

    for i in messages:
        key = START
        starrable_values[key].append(i[0])
        for j in range(len(i)):
            key += i[j]
            key = key[-STARRABLE_CONTEXT:]
            toadd = END
            try:
                toadd = i[j + 1]
            except:
                pass
            if key not in starrable_values:
                starrable_values[key] = [toadd]
                continue

            starrable_values[key].append(toadd)


def generate_afk_map():
    messages = []

    with open("./afk.json") as f:
        messages = json.loads(f.read())
        messages = [o.replace(START, "").replace(END, "") for o in messages if o != ""]

    afk_values[START] = []

    for i in messages:
        key = START
        afk_values[key].append(i[0])
        for j in range(len(i)):
            key += i[j]
            key = key[-AFK_CONTEXT:]
            toadd = END
            try:
                toadd = i[j + 1]
            except:
                pass
            if key not in afk_values:
                afk_values[key] = [toadd]
                continue

            afk_values[key].append(toadd)


def generate_starrable_message():
    message = START

    while True:
        message += random.choice(starrable_values[message[-STARRABLE_CONTEXT:]])
        if message[-1] == END:
            break

    return message[1:-1][0:100]


def generate_average_message():
    message = START

    while True:
        message += random.choice(average_values[message[-AVERAGE_CONTEXT:]])
        if message[-1] == END:
            break

    return message[1:-1][0:100]


def generate_afk_message():
    message = START

    while True:
        message += random.choice(afk_values[message[-AFK_CONTEXT:]])
        if message[-1] == END:
            break

    return message[1:-1][0:100]
