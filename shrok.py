import discord
from discord.ext import commands
import json
import urllib
from urllib.request import urlopen, Request
from urllib.parse import urlencode
description = '''Shrok CreamyMemers Discord DnD Bot'''
bot = commands.Bot(command_prefix=']', description=description)
@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name + " " + bot.user.id + "\n")

@bot.command()
async def commands():
    await bot.say("```===Help Text===\n]commands - Displays this text\n]d100 - Rolls a d100\n]d20 - Rolls a d20\n]d12 - Rolls a d12\n]d10 - Rolls a d10\n]d8 - Rolls a d8\n]d6 - Rolls a d6\n]d4 - Rolls a d4\n]d2 - Rolls a d2```")

@bot.command()
async def d20():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 20,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d20: " + z)

@bot.command()
async def d100():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 100,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d100: " + z)

@bot.command()
async def d12():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0"20,"method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 12,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d12: " + z)

@bot.command()
async def d10():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 10,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d10: " + z)

@bot.command()
async def d8():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 8,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d8: " + z)

@bot.command()
async def d6():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 6,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d6: " + z)

@bot.command()
async def d4():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 4,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d4: " + z)

@bot.command()
async def d2():
    await bot.say("Rolling :game_die: ...")
    jsonArgPrep = '{"jsonrpc": "2.0","method": "generateIntegers","params": {"apiKey": "3fbbd984-8ebe-4bc7-a695-dd892b22703e","n": 1,"min": 1,"max": 2,"replacement": true},"id": 42}'
    jsonArg = jsonArgPrep.encode('ascii')
    rawRequest = urlopen(Request('https://api.random.org/json-rpc/1/invoke', jsonArg))
    jsonRequest = json.loads(rawRequest.read().decode('utf-8'))
    print("\nAPI Response: \n" + str(jsonRequest))
    x = jsonRequest["result"]
    y = x["random"]
    z = y["data"]
    z = str(z)[1:-1]
    await bot.say("Result of d2: " + z)

bot.run("MzYxNjQyNzIxNzc5MTIyMTg3.DKnQvA.8CbY3sHLZc178ew7UzQUC8PHTgs")
