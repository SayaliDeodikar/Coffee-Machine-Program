from CoffeMachineData import menu, resources, logo
profit = 0

def check_resources(order_ingredients):
    '''Checks if the resources are sufficient to make coffe'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print('Insufficient resources to make coffee')
            exit(0)
    
def make_coffe(coffee_type,order_ingredients):
    '''Makes coffee and updates the resources'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


def calculate(quarters,dimes,nickles,pennies,coffee_type,amount): 
    ''' Calculates the total bill of customer, returns the change and calculate profit'''
    total = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01) 
    change = round((total - amount),2)  
    if total < amount:
        print("Sorry that's not enough money. Money refunded")
        exit(0)
    else:
        print(f"Here is {change} in change")
        global profit
        profit += amount

def process():
    '''Process the coffee maker'''
    choice = input("What would you like to have? (espresso/latte/cappuccino): ")
    if choice == 'off':
        exit(0)
    elif choice == 'report':
        for key in resources:
            print(f"{key}:{resources[key]}")
        print(f"profit:{profit}")
        
    else:
        ing = menu[choice]['ingredients']
        check_resources(ing)
        bill = menu[choice]['cost']
        print(f'Your bill: {bill}')
        print('Please insert coins :')
        quarters = int(input("How many quarters?: "))
        dimes =  int(input("How many dimes?: "))
        nickels =  int(input("How many nickels?: "))
        pennies =  int(input("How many pennies?: "))
        calculate(quarters,dimes,nickels,pennies,choice,bill)
        make_coffe(choice,ing)

print(logo)
is_on = True
while is_on:
    process()


