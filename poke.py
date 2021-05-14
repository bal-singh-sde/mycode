#!/usr/bin/env python3
import requests
import wget


def main():
    poke_name = input("what poke to look for? ").lower()
    try:
        poke_api = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}").json()
    except:
        print("Invalid poke")

    # image url
    url = poke_api['sprites']['front_default']
    print(url)

    wget.download(url, '/home/student/mycode/')

    for key in poke_api:
        if key == 'game_indices':
            print(len(key))

    for name in poke_api:
        if name == 'moves':
            for everydict in poke_api[name]:
                print(everydict['move']['name'])


main()
