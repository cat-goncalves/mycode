#!/usr/bin/env python3
# day 5 warmup: Friday May 20th, 2022

from classinfo import classinfo

def main():
    me = classinfo['all'][0]
    print(f"My name is {me['name']} and my skills are {me['skill level']}\n\n")

    for x in classinfo["all"]:
        name = x["name"]
        skillLevel = x['skill level']
        spiritAnimal = x["spirit animal"]
        superPower = x['super power']
        print(f"{name}, an {skillLevel} {spiritAnimal} of a programmer, posseses a {superPower} factor for moonligting as a superhero!")

main()