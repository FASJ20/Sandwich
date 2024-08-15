import pyinputplus as pyip


def choose_bread():
    bread_types = {'Wheat': 2.0, 'White': 2.5, 'Sourdough': 4.5}
    select_bread = pyip.inputChoice(
        choices=list(bread_types.keys()),
        prompt=f'Select your choice of bread {bread_types}: ',
        caseSensitive=False
    )
    return select_bread, bread_types[select_bread]

def choose_protein():
    meat_types = {"Chicken": 2.5, "Turkey": 3.0, "Ham": 1.5, "Tofu": 1.0}
    select_meat = pyip.inputChoice(
        choices=list(meat_types.keys()),
        prompt=f'Select your choice of meat {meat_types}: ',
        caseSensitive=False)
    return select_meat, meat_types[select_meat]


def choose_cheese():
    cheese_options = {"Cheddar": 1.0, "Swiss": 1.5, "Mozzarella": 2.5}
    select_cheese = pyip.inputChoice(
        choices=list(cheese_options.keys()),
        prompt=f'Select your choice of meat {cheese_options.items()}: ',
        caseSensitive=False)
    return select_cheese, cheese_options[select_cheese]


def calculate_total(bread_price, meat_price):



    return total_price_of_choices * num_sandwich


bread_choice, bread_price = choose_bread()
meat_choice, meat_price = choose_protein()

other_ingredients = pyip.inputYesNo(prompt="Will you like to add mayonnaise, tomato, mustard and lettuce?? ",
                                    caseSensitive=False)
cheese_yesno = pyip.inputYesNo(prompt="Do you want cheese?? ", caseSensitive=False)
if cheese_yesno == "yes":
    cheese_choice, cheese_price = choose_cheese()

    if other_ingredients == "yes":
        other_ingredients_price = 1

        total_price_of_choices = bread_price + meat_price + cheese_price + other_ingredients_price

        print("\nOrder Summary:")
        print(f"Bread: {bread_choice} (${bread_price:.2f})")
        print(f"Protein: {meat_choice} (${meat_price:.2f})")
        print(f"Cheese: {cheese_choice} (${cheese_price:.2f})")


    else:
        total_price_of_choices = bread_price + meat_price + cheese_price

        print("\nOrder Summary:")
        print(f"Bread: {bread_choice} (${bread_price:.2f})")
        print(f"Protein: {meat_choice} (${meat_price:.2f})")
        print(f"Cheese: {cheese_choice} (${cheese_price:.2f})")

elif cheese_yesno == "no":
    if other_ingredients == "yes":
        other_ingredients_price = 1.0

        total_price_of_choices = bread_price + meat_price + other_ingredients_price

        print("\nOrder Summary:")
        print(f"Bread: {bread_choice} (${bread_price:.2f})")
        print(f"Protein: {meat_choice} (${meat_price:.2f})")



    else:
        total_price_of_choices = bread_price + meat_price

        print("\nOrder Summary:")
        print(f"Bread: {bread_choice} (${bread_price:.2f})")
        print(f"Protein: {meat_choice} (${meat_price:.2f})")


else:
    total_price_of_choices = bread_price + meat_price
num_sandwich = pyip.inputNum(prompt="How many sandwiches do you want?? ")
total_price = calculate_total(bread_price, meat_price)
print(f"Total Price: ${total_price:.2f}")


