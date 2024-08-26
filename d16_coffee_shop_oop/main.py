from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_is_on = True

while machine_is_on:          
    order = input(f"What would you like? {menu.get_items()}?: ")
    if order == 'report':
        coffee_maker.report()
        money_machine.report()
    elif order == 'off':
        machine_is_on = False
    else:
        drink = menu.find_drink(order)
        if drink != "Sorry that item is not available.":
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)           
        else:
            print(drink)