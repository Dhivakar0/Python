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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
income = 0

def is_resource_enough(ordered_ingredients):
    '''Returns True if the resources are enough to make order and False if not'''
    for item in ordered_ingredients:
        if ordered_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    '''Returns the total amount paid by the customer'''
    total = int(input("how many quarters?: ")) *0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_payment_successful(money_received, drink_price):
    """Returns True if the money paid is accepted and False if not"""
    if money_received >= drink_price:
        change = round(money_received - drink_price, 2)
        print(f"Here is ${change} in change.")
        global income
        income += drink_price
        return True
    else:
        print(("Sorry that's not enough money. Money refunded."))
        return False


def make_coffee(drink_name, ordered_ingredients):
    """Deducts the resources after the successful order and makes coffee"""
    for item in ordered_ingredients:
        resources[item] -= ordered_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${income}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








