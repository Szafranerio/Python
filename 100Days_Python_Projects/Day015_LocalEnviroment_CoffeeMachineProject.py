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
            "water": 300,
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
    "tea": 200
}

while True:
    choice = input(
        'What would you like? (espresso/latte/cappuccino/americano/chocolate/tea): ').lower()
