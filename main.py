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

money = 0


def enough_resources(menu_options, choice, total_resources):
  '''Checks if what the user ordered can be produced with the current resources available
  and returns False if there is not enough resource. Else, returns true.'''
  for ingredient in menu_options[choice]["ingredients"]:
    quantity = menu_options[choice]['ingredients'][ingredient]
    if quantity > total_resources[ingredient]:
      print(f"Sorry, not enough {ingredient}.")
      return False

  return True


def receive_payment():
  coins_dict = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}
  coins_sum = 0
  print("Please insert coins.")
  for coin in coins_dict:
    inserted_coin = int(input(f"How many {coin}?:"))
    total = inserted_coin * coins_dict[coin]
    coins_sum += total
  return coins_sum


##### START ####

is_on = True

while is_on:
  order = input("What would you like? (espresso/latte/cappuccino): ")
  if order == "report":
    for resource in resources:
      print(f"{resource.capitalize()}: {resources[resource]}ml")
    print(f"Money available is {money}.")
  elif order == "off":
    is_on = False
  else:
      if enough_resources(MENU, order, resources):
        money_inserted = receive_payment()
        change = round(money_inserted - MENU[order]["cost"], 2)
        if change < 0:
          print("Sorry, that's not enough money. Money refunded.")
        else:
          print(f"The price of the {order} is {MENU[order]['cost']}.")
          print(f"Here is your change: $ {change}")
          print(f"Here is your {order}. ☕️ Enjoy!")
          for ingredient in MENU[order]["ingredients"]:
            quantity = MENU[order]['ingredients'][ingredient]
            resources[ingredient] = resources[ingredient] - quantity
          money += MENU[order]["cost"]


