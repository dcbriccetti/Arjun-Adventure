from random import randint
from time import time

dig_avail_at = time()
monk_eye = 0
depwith = True
money = 3932333
jail = False
bank = 0
shop_list = ['5,000:Shovel, 10,000:Phone, 20,000:Computer, 100,000:Cheese']
inventory = []
knowledge = 0
jobishere = 0


def game():
    global dig_avail_at
    global monk_eye
    global money
    global bank
    global shop_list
    global inventory
    global knowledge
    global jobishere
    global depwith
    elephant = randint(100, 1000)
    bunny = randint(300, 9000)
    monkey = randint(700, 10000)
    print('What do you want to do?')
    whattodo = input().lower()
    if whattodo == 'rob':
        print('Who would you like to rob? Elephant, bunny or monkey?')
        robinput = input().lower()
        dierob = randint(1, 100)
        if dierob <= 25:
            print('You died while robbing the', robinput)
            money = 0
            bank = 0
            inventory = []
            game()
        else:
            if robinput == 'elephant':
                robchance = randint(1, 100)
                if robchance >= 50:
                    print('You got', elephant, 'moneys')
                    money = elephant + money
                    print('You have', money, 'money')
                    game()
                if robchance <= 50:
                    print('The police caught you and you lost all your money!')
                    money = 0
                    bank = 0
                    inventory = []
                    game()
            if robinput == 'bunny':
                robchance = randint(1, 100)
                if robchance > 25:
                    print('You got', bunny, 'moneys')
                    money = bunny + money
                    print('You have', money, 'money')
                    game()
                if robchance <= 25:
                    print('The police caught you and you lost all your money!')
                    money = 0
                    bank = 0
                    game()
            if robinput == 'monkey':
                robchance = randint(1, 100)
                if robchance > 25:
                    print('You got', monkey, 'moneys')
                    money = monkey + money
                    print('You have', money, 'money')
                    game()
                if robchance < 25:
                    print('The police caught you and you lost all your money!')
                    money = 0
                    bank = 0
                    game()
    elif whattodo == 'gamble':
        gamblepick = randint(1, 3)
        if gamblepick == 1:
            print('Pick a number between 1 and 10')
            numberpicker = randint(1, 10)
            numberpick = int(input())
            if numberpick == numberpicker:
                gamblemoney = randint(1000, 10000)
                print('You won', gamblemoney, 'money')
                money = gamblemoney + money
                print('You have', money, 'money')
                game()
            else:
                gamblemoney = randint(1000, 4000)
                print('You lost', gamblemoney, 'money')
                money = money - gamblemoney
                print('You have', money, 'money')
                game()
        if gamblepick == 2:
            moneylost = randint(10, 1000)
            print('You lost', moneylost, 'money')
            money = money - moneylost
            print('You have', money, 'money')
            game()
        if gamblepick == 3:
            moneywon = randint(10, 10000)
            print('You won', moneywon, 'money')
            money = moneywon + money
            print('You have', money, 'money')
            game()
    elif whattodo == 'help':
        print('You can: rob, gamble, balance, deposit, withdraw, treasure, shop, inventory, sell, use, sports')
        game()
    else:
        print('Invalid action')
        game()


game()
