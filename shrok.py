import discord
from discord.ext import commands
import json
import urllib
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import random
description = '''Shrok CreamyMemers Discord DnD Bot'''
bot = commands.Bot(command_prefix=']', description=description)

def ModCalc(Ability):
    if Ability == 10 or Ability == 11:
        return 0
    elif Ability == 12 or Ability == 13:
        return 1
    elif Ability == 14 or Ability == 15:
        return 2
    elif Ability == 16 or Ability == 17:
        return 3
    elif Ability == 18 or Ability == 19:
        return 4
    elif Ability == 20 or Ability == 21:
        return 5
    elif Ability == 22 or Ability == 23:
        return 6
    elif Ability == 24 or Ability == 25:
        return 7
    elif Ability == 26 or Ability == 27:
        return 8
    elif Ability == 28 or Ability == 29:
        return 9
    elif Ability == 30:
        return 10

@bot.event
async def on_ready():
    print("INFO: Logged in as " + bot.user.name + " " + bot.user.id + "\n")

@bot.event
async def on_error(event, args):
    print("ERROR: \n    Event: " + str(event) + "\n    Argument: " + str(args))
    await bot.say("```Erorrs have Layers: " + str(event) + "```")

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

@bot.command()
async def randEnemy():
    HitDie = random.choice(range(2, 13, 2))
    Health = random.choice(range(1, 26))
    ArmorClass = random.choice(range(1, 9))
    Str = random.choice(range(10, 31))
    StrMod = ModCalc(Str)
    Dex = random.choice(range(10, 31))
    DexMod = ModCalc(Dex)
    Con = random.choice(range(10, 31))
    ConMod = ModCalc(Con)
    Int = random.choice(range(10, 31))
    IntMod = ModCalc(Int)
    Wis = random.choice(range(10, 31))
    WisMod = ModCalc(Wis)
    Cha = random.choice(range(10, 31))
    ChaMod = ModCalc(Cha)
    Init = random.choice(range(-4, 5))
    await bot.say("```     Hit Die: d" + str(HitDie) + \
        "\n          HP: " + str(Health) + \
        "\n          AC: " + str(ArmorClass) + \
        "\n  Initiative: " + str(Init) + \
        "\n----------------" + \
        "\n    Strength: " + str(Str) + \
        "\n   Dexterity: " + str(Dex) + \
        "\nConstitution: " + str(Con) + \
        "\nIntelligence: " + str(Int) + \
        "\n      Wisdom: " + str(Wis) + \
        "\n    Charisma: " + str(Cha) + \
        "\n----------------" + \
        "\n      StrMod: " + str(StrMod) + \
        "\n      DexMod: " + str(DexMod) + \
        "\n      ConMod: " + str(ConMod) + \
        "\n      IntMod: " + str(IntMod) + \
        "\n      WisMod: " + str(WisMod) + \
        "\n      ChaMod: " + str(ChaMod) + "```")

@bot.command()
async def expGain(basePokemonEXP, LVLFaintedPokemon, PlayerPokemonUsed):
    expGained = ( int(basePokemonEXP) * int(LVLFaintedPokemon) )/( 7 * int(PlayerPokemonUsed) )
    await bot.say("Experience Gained: " + str(int(expGained)) )
    
bot.run("API_TOKEN")
