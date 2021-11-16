from random import randint
from time import time

class Game:
    def __init__(self) -> None:
        self.elephant = randint(100, 1000)
        self.bunny = randint(300, 9000)
        self.monkey = randint(700, 10000)
        self.dig_avail_at = time()
        self.monk_eye = 0
        self.depwith = True
        self.money = 3932333
        self.jail = False
        self.bank = 0
        self.shop_list = ['5,000:Shovel, 10,000:Phone, 20,000:Computer, 100,000:Cheese']
        self.inventory = []
        self.knowledge = 0
        self.jobishere = 0
        self.actions = {
            'rob': self.rob,
            'gamble': self.gamble,
            'help': self.help,
        }

    def play(self):
        while True:
            print('What do you want to do?')
            whattodo = input().lower()
            if action_function := self.actions.get(whattodo):
                action_function()
            else:
                print('Invalid action')

    def rob(self):
        print('Who would you like to rob? Elephant, bunny or monkey?')
        robinput = input().lower()
        dierob = randint(1, 100)
        if dierob <= 25:
            print('You died while robbing the', robinput)
            self.money = 0
            self.bank = 0
            self.inventory = []
        else:
            if robinput == 'elephant':
                robchance = randint(1, 100)
                if robchance >= 50:
                    print('You got', self.elephant, 'moneys')
                    money = self.elephant + self.money
                    print('You have', money, 'money')
                if robchance <= 50:
                    print('The police caught you and you lost all your money!')
                    self.money = 0
                    self.bank = 0
                    self.inventory = []
            if robinput == 'bunny':
                robchance = randint(1, 100)
                if robchance > 25:
                    print('You got', self.bunny, 'moneys')
                    self.money = self.bunny + self.money
                    print('You have', self.money, 'money')
                if robchance <= 25:
                    print('The police caught you and you lost all your self.money!')
                    self.money = 0
                    self.bank = 0
            if robinput == 'monkey':
                robchance = randint(1, 100)
                if robchance > 25:
                    print('You got', self.monkey, 'moneys')
                    self.money = self.monkey + self.money
                    print('You have', self.money, 'money')
                if robchance < 25:
                    print('The police caught you and you lost all your self.money!')
                    self.money = 0
                    self.bank = 0

    def gamble(self):
        gamblepick = randint(1, 3)
        if gamblepick == 1:
            print('Pick a number between 1 and 10')
            numberpicker = randint(1, 10)
            numberpick = int(input())
            if numberpick == numberpicker:
                gamblemoney = randint(1000, 10000)
                print('You won', gamblemoney, 'money')
                self.money = gamblemoney + self.money
                print('You have', self.money, 'money')
            else:
                gamblemoney = randint(1000, 4000)
                print('You lost', gamblemoney, 'money')
                self.money = self.money - gamblemoney
                print('You have', self.money, 'money')
        if gamblepick == 2:
            moneylost = randint(10, 1000)
            print('You lost', moneylost, 'money')
            self.money = self.money - moneylost
            print('You have', self.money, 'money')
        if gamblepick == 3:
            moneywon = randint(10, 10000)
            print('You won', moneywon, 'money')
            self.money = moneywon + self.money
            print('You have', self.money, 'money')

    def help(self):
        print('You can: ' + ', '.join(self.actions.keys()))

Game().play()
