# Description
# Write a program that asks users for their sandwich preferences.
# The program should use PyInputPlus to ensure that they enter valid input, such as:
# 1. Using inputMenu() for a bread type: wheat, white, or sourdough.
# 2. Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# 3. Using inputYesNo() to ask if they want cheese.
# 4. If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# 5. Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# 6. Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.

# Come up with prices for each of these options,
# and have your program display a total cost after the user enters their selection.

import copy
import pyinputplus as pyip

ingredients = dict(
    breadType = ('Wheat', 'Wite', 'Sourdough'),
    proteinType = ('Chicken', 'Turkey', 'Ham', 'Tofu'),
    cheeseType = ('Cheddar', 'Swiss', 'Mozzarella'),
    addOns = ('Mayo', 'Mustard', 'Lettuce', 'Tomato')
)

sandwicheObject = dict(
    bread = '',
    protein = '',
    cheese = '',
    addOns = {key.lower(): True for key in ingredients['addOns']},
    quantity = 1,
)

def sandwichMaker():
    '''
        A function that guides the user through the process of creating a custom sandwich order.
    '''

    sandwich = copy.deepcopy(sandwicheObject)

    print('Welcome to our sandwich shop! Please follow the prompt to order your lunch')

    sandwich['bread'] = pyip.inputMenu(ingredients['breadType'], lettered = False, numbered = True)
    sandwich['protein'] = pyip.inputMenu(ingredients['proteinType'], lettered = False, numbered = True)
    sandwich['cheese'] = pyip.inputMenu(ingredients['cheeseType'], lettered = False, numbered = True)
    for addOn in ingredients['addOns']:
        customerChoice = pyip.inputYesNo(f'Do you want to add {addOn}?')
        sandwich['addOns'][addOn.lower()] = True if customerChoice == 'yes' else False
    sandwich['quantity'] = pyip.inputNum('How many sandwiches would you like to get today?', min=1)
    print(f'Here is a summary of your order: {sandwich}.\nThank you for ordering.')

def sandwichMakerLoopVerion():
    '''
        A function that guides the user through the process of creating a custom sandwich order.
    '''

    sandwich = copy.deepcopy(sandwicheObject)

    for ingredient in ingredients.keys():
            if ingredient.endswith('Type'):
                sandwichKey = ingredient.replace('Type', '').lower()
                sandwich[sandwichKey] = pyip.inputMenu(
                    ingredients[ingredient],
                    lettered=False,
                    numbered=True,
                )
            elif ingredient == 'addOns':
                for addOn in ingredients[ingredient]:
                    customerChoice = pyip.inputYesNo(f'Do you want to add {addOn}?')
                    sandwich[ingredient][addOn.lower()] = True if customerChoice == 'yes' else False

    sandwich['quantity'] = pyip.inputNum('How many sandwiches would you like to get today?', min=1)

    print(f'Here is a summary of your order: {sandwich}.\nThank you for ordering.')


# sandwichMaker()
sandwichMakerLoopVerion()
