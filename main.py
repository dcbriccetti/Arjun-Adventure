from random import randint
from time import time

class Game:
    def __init__(self) -> None:
        self.elephant = randint(100, 1000)
        self.bunny = randint(300, 9000)
        self.monkey = randint(700, 10000)
        self.dig_avail_at = time()
        self.monk_eye = 0
        self.dep_with = True
        self.money = 3932333
        self.jail = False
        self.bank = 0
        self.shop_list = ['5,000:Shovel, 10,000:Phone, 20,000:Computer, 100,000:Cheese']
        self.inventory = []
        self.knowledge = 0
        self.job_is_here = 0
        self.actions = {
            'rob': self.rob,
            'gamble': self.gamble,
            'help': self.help,
        }

    def play(self):
        while True:
            print('What do you want to do?')
            what_to_do = input().lower()
            if action_function := self.actions.get(what_to_do):
                action_function()
            else:
                print('Invalid action')

    def rob(self):
        print('Who would you like to rob? Elephant, bunny or monkey?')
        rob_input = input().lower()
        die_rob = randint(1, 100)
        if die_rob <= 25:
            print('You died while robbing the', rob_input)
            self.money = 0
            self.bank = 0
            self.inventory = []
        else:
            if rob_input == 'elephant':
                rob_chance = randint(1, 100)
                if rob_chance >= 50:
                    print('You got', self.elephant, 'moneys')
                    money = self.elephant + self.money
                    print('You have', money, 'money')
                else:
                    self.police_catch()
                    self.inventory = []
            if rob_input == 'bunny':
                rob_chance = randint(1, 100)
                if rob_chance > 25:
                    print('You got', self.bunny, 'moneys')
                    self.money += self.bunny
                    print('You have', self.money, 'money')
                else:
                    self.police_catch()
            if rob_input == 'monkey':
                rob_chance = randint(1, 100)
                if rob_chance > 25:
                    print('You got', self.monkey, 'moneys')
                    self.money += self.monkey
                    print('You have', self.money, 'money')
                else:
                    self.police_catch()

    def police_catch(self):
        print('The police caught you and you lost all your money!')
        self.money = 0
        self.bank = 0

    def gamble(self):
        gamble_pick = randint(1, 3)
        if gamble_pick == 1:
            print('Pick a number between 1 and 10')
            number_picker = randint(1, 10)
            number_pick = int(input())
            if number_pick == number_picker:
                gamble_money = randint(1000, 10000)
                print('You won', gamble_money, 'money')
                self.money += gamble_money
                print('You have', self.money, 'money')
            else:
                gamble_money = randint(1000, 4000)
                print('You lost', gamble_money, 'money')
                self.money -= gamble_money
                print('You have', self.money, 'money')
        elif gamble_pick == 2:
            money_lost = randint(10, 1000)
            print('You lost', money_lost, 'money')
            self.money -= money_lost
            print('You have', self.money, 'money')
        elif gamble_pick == 3:
            money_won = randint(10, 10000)
            print('You won', money_won, 'money')
            self.money += money_won
            print('You have', self.money, 'money')

    def help(self):
        print('You can: ' + ', '.join(self.actions.keys()))

Game().play()
