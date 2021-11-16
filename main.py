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
    elif whattodo == 'balance':
        print('You have', money, 'money')
        print('You have', bank, 'money in the bank')
        game()
    elif whattodo == 'deposit':
        if depwith:
            print('You have', money, 'money')
            print('How much do you want to deposit?')
            depositamount = int(input())
            money = money - depositamount
            bank = depositamount + bank
            print('You have', money, 'money')
            print('You have', bank, 'money in the bank')
            print('Deposit complete!')
            game()
        else:
            print('You robbed the bank so the bank is mad at you. You cant deposit or withdraw anymore.')
            game()
    elif whattodo == 'help':
        print('You can: rob, gamble, balance, deposit, withdraw, treasure, shop, inventory, sell, use, sports')
        game()
    elif whattodo == 'withdraw':
        if depwith:
            if bank == 0:
                print('You cant withdraw anything. First deposit something.')
                game()
            else:
                print('You have', money, 'money')
                print('You have', bank, 'money in the bank')
                print('How much do you want to withdraw?')
                withdraw = int(input())
                bank = bank - withdraw
                money = money + withdraw
                print('You have', money, 'money')
                print('You have', bank, 'money in the bank')
                game()
        else:
            print('You robbed the bank so the bank is mad at you. You cant deposit or withdraw anymore.')
            game()
    elif whattodo == 'treasure':
        print('You go through the forest looking for treasure!')
        treasure = randint(1, 100)
        if treasure <= 25:
            treasureamount = randint(3, 300000)
            print('You got', treasureamount, 'money')
            money = money + treasureamount
            print('You have', money, 'money')
            game()
        elif treasure > 25 and treasure <= 50:
            print('You died and lost everything!')
            money = 0
            bank = 0
            inventory = []
        else:
            print('You didnt get anything')
            game()
    elif whattodo == 'shop':
        print(','.join(shop_list))
        buy = str(input())
        if buy == 'phone':
            if money > 10000:
                print('You bought the phone for 10,000 dollars')
                money = money - 10000
                print('You have', money, 'money')
                inventory.append('phone')
                game()
            else:
                print('You dont have enough money to buy this.')
                game()
        if buy == 'computer':
            if money > 20000:
                print('You bought the compouter for 20,000 dollars')
                money = money - 20000
                print('You have', money, 'money')
                inventory.append('computer')
                game()
            else:
                print('You dont have enough money to buy this.')
                game()
        if buy == 'cheese':
            if money > 100000:
                print('Why would you buy cheese for 100,000 dollars?')
                money = money - 100000
                print('You have', money, 'money')
                inventory.append('cheese')
                game()
            else:
                print('You dont have enough money to buy this.')
                game()
        if buy == 'shovel':
            if money >= 5000:
                print('You have a shovel. You can use it using the dig command.')
                inventory.append('shovel')
                money = money - 5000
                print('You have', money, 'money')
                game()
            else:
                print('You dont have enough money to buy this.')
                game()
        if buy == 'exit':
            game()
    elif whattodo == 'inventory':
        print(','.join(inventory))
        game()
    elif whattodo == 'sell':
        print('What do you want to sell in your inventory?', ','.join(inventory))
        sellitem = str(input()).lower()
        if sellitem in inventory:
            sellchance = randint(1000, 10000)
            print('You sold it to someone for', sellchance, 'dollars')
            inventory.remove(sellitem)
            game()
        if sellitem == 'exit':
            game()
        else:
            print('You dont have that in your inventory')
            game()
    elif whattodo == 'use':
        print('What do you want to use')
        use = str(input())
        if use == 'phone':
            if 'phone' in inventory:
                print('You can either call the police or the cia')
                usephone = str(input())
                if usephone == 'police':
                    print('The police got mad at you for calling.')
                    jailchance = randint(1, 100)
                    if jailchance >= 30:
                        game()
                    if jailchance < 30:
                        print('You went to jail and lost all of your money')
                        money = 0
                        bank = 0
                        inventory = []
                        game()
                if usephone == 'cia':
                    print('The cia tracked you down and are now chasing you')
                    print('You can either hide in an alley or let them catch you')
                    chase = str(input())
                    if chase == 'alley':
                        print('The cia didnt find you and you survived')
                        game()
                    if chase == 'catch':
                        print('They caught you and took all your money')
                        money = 0
                        bank = 0
                        inventory = []
                        game()
            else:
                print('You dont have phone')
                game()
        if use == 'computer':
            if 'computer' in inventory:
                print('Turns out, your computer doesnt work')
                game()
            else:
                print('You dont have a computer')
                game()
        if use == 'cheese':
            if 'cheese' in inventory:
                print('You ate the cheese. It was yummy.')
                game()
            else:
                print('You dont have cheese')
                game()
        if use == 'shovel':
            if 'shovel' in inventory:
                print('To use the shovel use the: dig :command.')
                game()
    elif whattodo == 'sleep':
        sleepchance = randint(1, 100)
        if sleepchance >= 30:
            print('You fell asleep peacefully and woke up with 500 more dollars')
            money = money + 500
            game()
        elif sleepchance < 30 and sleepchance >= 10:
            print('Your money doubles for some reason')
            money = money * 2
            print('You have', money, 'money')
            game()
        else:
            print('You die')
            money = 0
            bank = 0
            inventory = []
            game()
    elif whattodo == 'monkey':
        if monk_eye == 1:
            print('You have already used this command.')
            game()
        else:
            print('YOU SAID THE MAGIC WORD YOU GET 10x YOUR MONEY! ONE TIME USE ONLY!')
            monk_eye = 1
            money = money * 10
            print('You have', money, 'money')
            game()
    elif whattodo == 'dance':
        dancerandom = randint(1, 10)
        if dancerandom == 1:
            print('You do zumba')
            zumba = randint(1, 100)
            if zumba > 50:
                print('You died while dancing.')
            if zumba < 50:
                print('For some reason you stopped dancing and started taking a shower')
                game()
        elif dancerandom == 2:
            print('You start doing fortnite dances and everyone beats you up')
            print('You lose half of your money')
            money = money / 2
            print('You have', money, 'money')
            game()
        elif dancerandom == 3:
            print('You get bullied by your friends for dancing')
            print('Oh yeah, they also took all of your money')
            money = 0
            print('You have', money, 'money')
            game()
        elif dancerandom == 4:
            print('You dont dance and instead play clash royale.')
            print('The gods of clash royale are happy so they give you 20k money')
            money = money + 20000
            print('You have', money, 'money')
            game()
        elif dancerandom == 5:
            print('You die while dancing')
            money = 0
            bank = 0
            inventory = []
            game()
        elif dancerandom > 6:
            print('You dance and then faint on the floor and lose 1k money')
            money = money - 1000
            print('You have', money, 'money')
            game()
        elif dancerandom == 6:
            moneydance = randint(1, 10000)
            print('You gain', moneydance, ' for dancing')
            game()
    elif whattodo == 'read':
        knowledgechance = randint(1, 50)
        if knowledgechance >= 18:
            print('You gained 1 knowledge')
            knowledge = knowledge + 1
            game()
        else:
            print('The book you read was boring. You lost a knowledge')
            knowledge = knowledge - 1
            game()
    elif whattodo == 'knowledge':
        print('Once you get 10 knowledge you can apply for a job using the job command.')
        print('You currently have', knowledge, 'knowledge')
        game()
    elif whattodo == 'dig':
        if time() > dig_avail_at:
            if 'shovel' in inventory:
                dig_avail_at = time() + 5
                digchance = randint(1, 100)
                if digchance >= 65:
                    digitem = randint(1, 7)
                    if digitem == 2:
                        print('You found a diamond')
                        inventory.append('diamond')
                    if digitem == 3:
                        print('You found a worm')
                        inventory.append('worm')
                        game()
                    if digitem == 5:
                        print('You found silver')
                        inventory.append('silver')
                        game()
                    else:
                        print('You didnt find anything')
            else:
                print('You dont have a shovel. Buy one from the shop.')
                game()
        else:
            print('You can dig in 5 seconds')
            game()
    elif whattodo == 'work':
        if jobishere == 1:
            workcheck = randint(1, 1000)
            workcheck2 = randint(1, 1000)
            workadder = workcheck + workcheck2
            print('What is', workcheck, '+', workcheck2)
            workanswer = int(input())
            if workanswer == workadder:
                print('Good Job! Heres 10k dollars')
                money = money + 10000
                print('You have', money, 'money')
                game()
            else:
                print('You got the answer wrong. Sorry!')
                game()
        else:
            print('You havent applied yet. Apply by using the command job.')
            game()
    elif whattodo == 'quit':
        print('Are you sure you want to leave. You will lose all your progress.')
        leave = str(input())
        if leave == 'yes':
            print('Bye!')
            quit()
        else:
            game()
    elif whattodo == 'job':
        if knowledge >= 10:
            jobpicker = randint(1, 3)
            jobishere = 1
            print('You can apply for a job. Here is your only option.')
            if jobpicker == 1:
                print('Firefighter')
            if jobpicker == 2:
                print('Artist')
            if jobpicker == 3:
                print('Homeless Man')
            print('Would you like to apply?')
            jobreply = str(input()).lower()
            if jobreply == 'yes':
                print('Okay. Here is your first 10000 paycheck! Work by using the work command!')
                money = money + 10000
                print('You have', money, 'money')
                jobishere = 1
                game()
            else:
                print('Your knowledge got deleted because you didnt want that job')
                game()
        else:
            print('You need 10 knowledge to get a job. Earn knowledge by using the read command.')
            game()
    elif whattodo == 'tip':
        tipchance = randint(1, 5)
        if tipchance == 5:
            print('When you sell something it will probably be sold for a really low price.')
            game()
        elif tipchance == 4:
            print('You can use the command: monkey : for 10x the money.')
            game()
        elif tipchance == 3:
            print('If you read enough using the : read : command, you can get a job.')
            game()
        elif tipchance == 2:
            print(
                'If you use the command: treasure :there is a chance you can get a very high amoung of money. Or you could lose all of your money.')
            game()
        else:
            print('Use the: help :command to see all commands.')
            game()
    elif whattodo == 'bankrob':
        if depwith:
            print(
                'Note: Once you rob the bank you will never be able to deposit or withdraw anything. Would you like to continue?')
            bankcheck = str(input()).lower()
            if bankcheck == 'yes':
                depwith = False
                bankliveordie = randint(1, 50)
                if bankliveordie >= 10:
                    print('You will have to answer a question to rob the bank.')
                    number1 = randint(1, 1000)
                    number2 = randint(1, 1000)
                    numbercalculatebank = number1 + number2
                    print('What is', number1, '+', number2)
                    bankadd = int(input())
                    if bankadd == numbercalculatebank:
                        bankmoney = randint(10000, 100000)
                        print('You won', bankmoney, 'money')
                        money = money + bankmoney
                        print('You have', money, 'money')
                        game()
                    else:
                        print('You got the question wrong and the police found you. You lost everything.')
                        money = 0
                        bank = 0
                        inventory = []
                        print('You have', money, 'money')
                        depwith = False
                        game()
                else:
                    print('You died and lost everything')
                    money = 0
                    inventory = []
                    bank = 0
                    game()
            else:
                print('You gained 1000 dollars for doing the right thing')
                money = money + 1000
                print('You have', money, 'money')
                game()
        else:
            print('You have already robbed the bank so you cant rob it again')
            game()
    elif whattodo == 'museum':
        print('Would you like to rob the museum? You might lose half of your money and also get a little surprise ;)')
        museumcheck = str(input()).lower()
        if museumcheck == 'yes':
            museumchance = randint(1, 4)
            if museumchance == 1:
                print('You got unlucky and lost half of your money. You didnt get anything')
                money = money / 2
                print('You have', money, 'money')
                game()
            else:
                museummoney = randint(1000, 40000)
                print('You robbed the museum for', museummoney, 'money')
                money = museummoney + money
                print('You have', money, 'money')
                game()
        else:
            print('Good Choice!')
            game()
    else:
        print('Invalid action')
        game()


game()
