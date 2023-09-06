from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# создаем переменные, в т.ч. переменные объекты, наследуемые от классов
is_on = True
my_menu = Menu()
my_coffeemaker = CoffeeMaker()
my_moneyMachine = MoneyMachine()
moneyInserted = 0
drink = ""
READY = False



# TODO 1: What you would like (espresso, latte, cappuccino)?
while is_on:
    choice = input(f"Вас приветствует кофе-машина для Аналитика. Что желаете {my_menu.get_items()}? ").lower()

    # TODO 2: If it's "off" then machine will turned off
    if choice == "off":
        print("Всего хорошего!")
        is_on = False

    # TODO 3: Print report, if input is "report"
    elif choice == "report":
        print("На текущий момент в кофе машине есть:")
        my_coffeemaker.report()
        my_moneyMachine.report()


    # TODO 4: Check resources. When drink is chosen, machine checks if there's enough products
    #         If it isn't, it should displays "Not enough {Product}"
    # elif choice == "espresso" or choice == "cappuccino" or choice == "latte":
    elif my_menu.find_drink(choice) is not None:
        drink = my_menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(drink):
            # TODO 5: Process coins. If there are enough resources, machine should take money
            #         and calculate the sum of it
            # moneyInserted = my_moneyMachine.process_coins()
            # print(f"Было внесено {moneyInserted} рублей")

            # TODO 6: Check transaction successful? If there's not enough money, you should refund it.
            #         If there's enough, you should take it, and give back change.
            # my_moneyMachine.make_payment(drink.cost)
            if my_moneyMachine.make_payment(drink.cost):
                # TODO 7: Make coffee. Show the user that coffee was made
                my_coffeemaker.make_coffee(drink)
