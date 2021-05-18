#!/usr/bin/env python3

import requests


def main():
    r = requests.get("http://api.open-notify.org/astros.json").json()

    print("People in space:", r['number'])

    for i in r['people']:
        print(i['name'], "is on the", i['craft'])


# if __name__ = "__main__":
main()

