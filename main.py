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

while is_on:
    choice = input(f"Вас приветствует кофе-машина для Аналитика. Что желаете {my_menu.get_items()}? ").lower()

    if choice == "off":
        print("Всего хорошего!")
        is_on = False

    elif choice == "report":
        print("На текущий момент в кофе машине есть:")
        my_coffeemaker.report()
        my_moneyMachine.report()
    elif my_menu.find_drink(choice) is not None:
        drink = my_menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(drink):

            if my_moneyMachine.make_payment(drink.cost):
                # TODO 7: Make coffee. Show the user that coffee was made
                my_coffeemaker.make_coffee(drink)
