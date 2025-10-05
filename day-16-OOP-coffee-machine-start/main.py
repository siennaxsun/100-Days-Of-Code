from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menus = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
options = menus.get_items()
while is_on:
    user_order = input(f"What drink would you like to order?: {options}\n").lower()
    if user_order == "off":
        is_on = False
    elif user_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menus.find_drink(user_order)  # output latte if it's in the menu
        print(drink)
        drink_price = drink.cost
        if coffee_maker.is_resource_sufficient(drink):
            # process coins
            # check if transaction successful
            # make coffee, deduct resources, calculate profits
            if money_machine.make_payment(drink_price):
                coffee_maker.make_coffee(drink)

        else:
            coffee_maker.is_resource_sufficient(drink)