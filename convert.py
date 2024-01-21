import argparse
import requests
from pathlib import Path

def main():
    cards = {}

    parser = argparse.ArgumentParser(prog="YDK to TCG Mass Entry",
                                    description="Program to convert your YDK file into a decklist you can copy/paste into TCG Mass Entry")
    parser.add_argument("-f", required=True, help="Provide file to convert")
    args = parser.parse_args()
    argsDict = vars(args)

    filepath = Path(argsDict["f"])
    file = open(filepath)

    for line in file.readlines():
        if(line[0].isdigit()):
            if(line.rstrip() in cards):
                cards[line.rstrip()] += 1
            else:
                cards[line.rstrip()] = 1

    res = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php")
    data = res.json()

    for card in cards:
        for item in data["data"]:
            if(str(item["id"]) == card):
                print(f"{cards[card]} {item['name']}")

if(__name__ == "__main__"):
    main()