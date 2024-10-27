from coffeemachine.main import make_coffee
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? {option}: ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(choice)



