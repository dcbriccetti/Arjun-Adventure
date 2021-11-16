from random import randint

class Game:
    def __init__(self) -> None:
        self.money = 3932333
        self.actions = {
            'rob': self.rob,
            'gamble': self.gamble,
            'help': self.help,
        }

    def play(self):
        while True:
            what_to_do = input('What do you want to do?').lower()
            if action_function := self.actions.get(what_to_do):
                action_function()
            else:
                print('Invalid action')

    def rob(self):
        rob_input = input('Who would you like to rob? Elephant, bunny or monkey?').lower()
        die_rob = randint(1, 100)
        if die_rob <= 25:
            print('You died while robbing the', rob_input)
            self.money = 0
            self.bank = 0
            self.inventory = []
        else:
            rob_chance = randint(1, 100)
            if rob_input == 'elephant':
                elephant = randint(100, 1000)
                if rob_chance >= 50:
                    self.apply_gain(elephant)
                else:
                    self.police_catch()
                    self.inventory = []
            elif rob_input == 'bunny':
                bunny = randint(300, 9000)
                if rob_chance > 25:
                    self.apply_gain(bunny)
                else:
                    self.police_catch()
            elif rob_input == 'monkey':
                monkey = randint(700, 10000)
                if rob_chance > 25:
                    self.apply_gain(monkey)
                else:
                    self.police_catch()

    def apply_gain(self, gain):
        print('You got', gain, 'moneys')
        self.money += gain
        self.show_money()

    def show_money(self):
        print(f'You have {self.money:,} money')

    def police_catch(self):
        print('The police caught you and you lost all your money!')
        self.money = 0
        self.bank = 0

    def gamble(self):
        gamble_pick = randint(1, 3)
        if gamble_pick == 1:
            number_picker = randint(1, 10)
            number_pick = int(input('Pick a number between 1 and 10'))
            if number_pick == number_picker:
                gamble_money = randint(1000, 10000)
                print('You won', gamble_money, 'money')
                self.money += gamble_money
                self.show_money()
            else:
                gamble_money = randint(1000, 4000)
                print('You lost', gamble_money, 'money')
                self.money -= gamble_money
                self.show_money()
        elif gamble_pick == 2:
            money_lost = randint(10, 1000)
            print('You lost', money_lost, 'money')
            self.money -= money_lost
            self.show_money()
        elif gamble_pick == 3:
            money_won = randint(10, 10000)
            print('You won', money_won, 'money')
            self.money += money_won
            self.show_money()

    def help(self):
        print('You can: ' + ', '.join(self.actions.keys()))

Game().play()
