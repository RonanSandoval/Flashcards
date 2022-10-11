import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cards = []

rows = [line.rstrip() for line in open('cards.csv', encoding='utf-8')]

for row in rows:
    cards.append(row.split(','))

random.shuffle(cards)

mode = input("Set mode? (1, 2, 3)")

for i in range(len(cards)):
    cls()
    print("------------------------------------------")
    print("Card", i + 1, "of", len(cards), '\n')
    if mode == "1":
        print(cards[i][0])
        input()
        print(cards[i][1])
    elif mode == "2":
        print(cards[i][1])
        input()
        print(cards[i][0])
    else:
        if random.randint(0, 1) == 0:
            print(cards[i][0])
            input()
            print(cards[i][1])
        else:
            print(cards[i][1])
            input()
            print(cards[i][0])
    input()

print("Done!")