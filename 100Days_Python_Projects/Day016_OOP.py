# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('DarkGoldenrod1')
# timmy.forward(100)
#
# my_screen = Screen()
#
# my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("Pokemon", ['Pikachu', 'Squirtle', 'Charmander'])
# table.add_column("Type", ['Electrical', 'Water', 'Fire'])
# table.align ['Pokemon'] = 'l'
# table.align['Type'] = 'r'
# table.border = True
# table.header = True
# print(table)


# OOP Coffee Machine
"""Files for modules are in the object oriented programming file,.
        They have to be connected in one file when using!!!!
    """
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like?: ({options}) ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
