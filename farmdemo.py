i#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

yuck = ["carrots", "celery"]
def neFarm():
    for x in farms[0]['agriculture']:
        print(x)


def whichFarm():
    choice = int(input("\nPick a number for farm: \n 0-> NE Farm \n 1-> W Farm \n 2-> SE Farm\n"))
    for x in farms[choice]['agriculture']:
        print(x)

def chooseFarm():
    choice = int(input("\nPick a number for farm: \n 0-> NE Farm \n 1-> W Farm \n 2-> SE Farm\n"))
    


neFarm()
whichFarm()
chooseFarm()
