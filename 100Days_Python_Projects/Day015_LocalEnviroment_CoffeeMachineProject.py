MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
    "americano":  {
        "ingredients": {
            "water": 250,
            "milk": 0,
            "coffee": 30,
        },
        "cost": 2.0,
    },
    "chocolate": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "chocolate": 50,
        },
        "cost": 1.5,
    },
    "tea": {
        "ingredients": {
            "water": 100,
            "milk": 0,
            "tea": 50,
        },
        "cost": 2.0,
    },
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "chocolate": 100,
    "tea": 90
}


def is_resources_sufficient(order):
    is_enough = True
    for item in order:
        if order[item] >= resources[item]:
            print(f'Sorry not enough {item}.')
            is_enough = False
    return is_enough


def calculate_coins():
    """Returns total amount of coins"""
    print('Please enter coins:')
    total = int(input('How many quaters ($0.25): ')) * 0.25
    total += int(input('How many dimes ($0.10): ')) * 0.10
    total += int(input('How many nickles ($0.05): ')) * 0.05
    total += int(input('How many pennies ($0.01): ')) * 0.01
    return total


def is_transaction_succesful(money_recived, drink_cost):
    """Return True is ayment is accepted or False if not"""
    if money_recived >= drink_cost:
        change = round(money_recived - drink_cost, 2)
        print(f'This is your {change} change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Not enough money')
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'This is your {drink_name}')


def refill(resources):
    """Refill by adding 500 of each"""
    for item in resources:
        resources[item] += 500
    print(f'The resources for {resources} has been added.')


def alert_check(resources):
    """Alert when low of resources"""
    for item, amount in resources.items():
        if amount < 50:
            print(
                f'Warning {item} is running low only {amount} left! Type refill.')


is_on = True

while is_on:
    choice = input(
        'What would you like? (espresso/latte/cappuccino/americano/chocolate/tea): ').lower()
    if choice == "off":
        is_on = False
        print('Switched off')
    elif choice == 'report':
        print(f"Water: {resources['water']} ml.")
        print(f"Milk : {resources['milk']} ml.")
        print(f"Coffee : {resources['coffee']} grams.")
        print(f"Chocolate : {resources['chocolate']} grams.")
        print(f"Tea: {resources['tea']} grams.")
        print(f"Money: ${profit}")
    elif choice == "refill":
        updated_resources = refill(resources)
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink['ingredients']):
            payment = calculate_coins()
            if is_transaction_succesful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])

        if alert_check(resources):
            print(alert_check)