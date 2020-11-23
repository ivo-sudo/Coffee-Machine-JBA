class CoffeeMachine:

    def __init__(self, water_level, coffee_level, milk_level, plastic_cups, money_level):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.plastic_cups = plastic_cups
        self. money_level = money_level

    water_level = 400
    coffee_level = 120
    milk_level = 540
    plastic_cups = 9
    money_level = 550

    def remaining():

        print(f'''The machine has:
{CoffeeMachine.water_level} of water
{CoffeeMachine.milk_level} of milk
{CoffeeMachine.coffee_level} of coffee beans
{CoffeeMachine.plastic_cups} of disposable cups
${CoffeeMachine.money_level} of money\n''')
        CoffeeMachine.main_method()

    def make_espresso():
        if CoffeeMachine.plastic_cups != 0 and CoffeeMachine.water_level >= 350 and CoffeeMachine.coffee_level >= 20 and CoffeeMachine.milk_level >= 75:
            print('I have enough resources, making you a coffee!\n')
            CoffeeMachine.water_level -= 250
            CoffeeMachine.coffee_level -= 16
            CoffeeMachine.money_level += 4
            CoffeeMachine.plastic_cups -= 1
            CoffeeMachine.main_method()
        elif CoffeeMachine.water_level < 250:
            print('Sorry, not enough water!\n')
            CoffeeMachine.main_method()
        elif CoffeeMachine.coffee_level < 16:
            print('Sorry, not enough coffee!\n')
            CoffeeMachine.main_method()

    def make_latte():
        if CoffeeMachine.plastic_cups != 0 and CoffeeMachine.water_level >= 350 and CoffeeMachine.coffee_level >= 20 and CoffeeMachine.milk_level >= 75:
            print('I have enough resources, making you a coffee!\n')
            CoffeeMachine.water_level -= 350
            CoffeeMachine.coffee_level -= 20
            CoffeeMachine.milk_level -= 75
            CoffeeMachine.money_level += 7
            CoffeeMachine.plastic_cups -= 1
            CoffeeMachine.main_method()
        elif CoffeeMachine.water_level < 350:
            print('Sorry, not enough water!\n')
            CoffeeMachine.main_method()
        elif CoffeeMachine.coffee_level < 20:
            print('Sorry, not enough coffee!\n')
            CoffeeMachine.main_method()
        elif CoffeeMachine.milk_level < 75:
            print('Sorry, not enough milk\n')
            CoffeeMachine.main_method()

    def make_cappuccino():
        if CoffeeMachine.plastic_cups != 0 and CoffeeMachine.water_level >= 200 and CoffeeMachine.coffee_level >= 12 and CoffeeMachine.milk_level >= 100:
            print('I have enough resources, making you a coffee!\n')
            CoffeeMachine.water_level -= 200
            CoffeeMachine.coffee_level -= 12
            CoffeeMachine.milk_level -= 100
            CoffeeMachine.money_level += 6
            CoffeeMachine.plastic_cups -= 1
            CoffeeMachine.main_method()
        elif CoffeeMachine.water_level < 200:
            print('Sorry, not enough water!\n')
            CoffeeMachine.main_method()
        elif CoffeeMachine.coffee_level < 12:
            print('Sorry, not enough coffee!\n')
            CoffeeMachine.main_method()
        elif CoffeeMachine.milk_level < 100:
            print('Sorry, not enough milk\n')
            CoffeeMachine.main_method()

    def main_method():
        action = input('Write action (buy, fill, take, remaining, exit):\n')
        print('\n')

        if action == 'buy':
            status = 'buying'
            choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n')
            if choice == '1':
                CoffeeMachine.make_espresso()
            elif choice == '2':
                CoffeeMachine.make_latte()
            elif choice == '3':
                CoffeeMachine.make_cappuccino()
            elif choice == 'back':
                CoffeeMachine.main_method()

        elif action == 'fill':
            status = 'restocking'
            added_water = int(input('Write how many ml of water do you want to add:\n'))
            added_milk = int(input('Write how many ml of milk do you want to add:\n'))
            added_coffee = int(input('Write how many grams of coffee beans do you want to add:\n'))
            added_cups = int(input('Write how many disposable cups of coffee do you want to add:\n'))

            CoffeeMachine.water_level += added_water
            CoffeeMachine.milk_level += added_milk
            CoffeeMachine.coffee_level += added_coffee
            CoffeeMachine.plastic_cups += added_cups

            CoffeeMachine.main_method()

        elif action == 'take':
            print(f'I gave you ${CoffeeMachine.money_level}')
            CoffeeMachine.money_level = 0
            CoffeeMachine.main_method()
        elif action == 'remaining':
            CoffeeMachine.remaining()
            print('\n')

        elif action == 'back':
            CoffeeMachine.main_method()
        elif action == 'exit':
            exit()


CoffeeMachine.main_method()
