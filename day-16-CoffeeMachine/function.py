# TODO: create a function to return required resources based on user's order
def required_resource(order):
    """check how much each ingredient is required for the order and return a dictionary"""
    required_resource = MENU[order]["ingredients"]
    if "water" in required_resource:
        required_water = required_resource["water"]
    else:
        required_resource["water"] = 0
    if "milk" in required_resource:
        required_milk = required_resource["milk"]
    else:
        required_resource["milk"] = 0
    if "coffee" in required_resource:
        required_coffee = required_resource["coffee"]
    else:
        required_resource["coffee"] = 0
    return required_resource



# TODO: check how many resources are left after the order
def check_resource_left(previous_resource_left, resource_used):
    """check how many resources are currently left and return a dictionary"""
    current_resource_left = {}
    previous_water_left = previous_resource_left["water"]
    previous_milk_left = previous_resource_left["milk"]
    previous_coffee_left = previous_resource_left["coffee"]
    water_left = previous_water_left - resource_used["water"]
    milk_left = previous_milk_left - resource_used["milk"]
    coffee_left = previous_coffee_left - resource_used["coffee"]
    current_resource_left["water"] = water_left
    current_resource_left["milk"] = milk_left
    current_resource_left["coffee"] = coffee_left
    return current_resource_left


# TODO: compare required resource from the order against the resources left
def check_resource_sufficient(required_resource, resource_left):
    """calculate whether resources are sufficient for the order, return boolean"""
    if resource_left["water"] - required_resource["water"] >= 0:
        #water sufficient
        if resource_left["milk"] - required_resource["milk"] >= 0:
            #milk sufficient
            if resource_left["coffee"] - required_resource["coffee"] >= 0:
                #coffee sufficient, can prompt user to inser coints
                return "True"
            else:
                return "Sorry, there's not enough coffee."
                # return False
        else:
            return "Sorry, there's not enough milk."
            # return False
    else:
        return "Sorry, there's not enough water."
        # return False


# TODO: generate insert coins prompts after the user insert some coins
QUARTERS = 0.25
DIMES = 0.10
NICKLE = 0.05
PENNY = 0.01
def insert_coins():
    """prompt user to insert quarters, dimes, nickles and pennies, and return paid amount"""
    user_paid = 0
    quarter_insert = int(input("how many quarters? "))
    user_paid += QUARTERS * quarter_insert
    dimes_insert = int(input("how many dimes? "))
    user_paid += DIMES * dimes_insert
    nickle_insert = int(input("how many nickles? "))
    user_paid += NICKLE * nickle_insert
    penny_insert = int(input("how many pennies? "))
    user_paid += PENNY * penny_insert
    return user_paid


# TODO: create a function to calculate if user pays enough for the order
def check_payment(order, user_paid, order_price):
    """check if the coins inserts are enough for the order and return feedback messages"""
    if user_paid < order_price:
        return "Sorry that's not enough money. Money refunded."
    else:
        change = round(user_paid - order_price, 2)
        return f"You have paid: {round(user_paid, 2)}. Here is ${change} in change.\nHere is your {order} Enjoy!"

