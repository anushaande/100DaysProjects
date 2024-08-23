resources = {'Water': 300,
             'Milk': 200,
             'Coffee':100,}
recipe_requirements = {'espresso': {'Water': 50,
                                    'Coffee': 18,
                                    'Milk': 0},
                        'latte' : {'Water' : 200,
                                   'Coffee' : 24,
                                   'Milk' : 150},
                        'cappuccino': {'Water' : 250,
                                       'Coffee' : 24,
                                        'Milk' : 100}, }
product_cost = {'espresso' : 1.50,
                'latte' : 2.50,
                'cappuccino': 3.00,}
machine_is_on = True
money = 0

def print_report(dict1, profit):
    for resource in dict1:
        if resource == 'Water':
            print(f"{resource}: {resources[resource]}ml")
        elif resource == 'Milk':
            print(f"{resource} : {resources[resource]}ml")
        elif resource == "Coffee":
            print(f"{resource} : {resources[resource]}g")
    print(f"profit : ${profit}")

def pay(choice):
    print(f"Please make the payment of {product_cost[choice]}")
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.5) + (pennies * 0.1)
    if total == product_cost[choice]:
        payment_successful = True
        text = "Paid" 
    elif total < product_cost[choice]:
        payment_successful = False
        text = "Sorry that's not enough money. Money refunded."
    else:
        payment_successful = True
        text = f"Here is ${round(total - product_cost[choice], 2)} in change."    
    return [text, payment_successful]

def check_resources(choice, dict1):
    if (dict1['Water'] < recipe_requirements[choice]['Water']):
        return "Sorry there is not enough water!"
    elif (dict1['Milk'] < recipe_requirements[choice]['Milk']):
        return "Sorry there is not enough Milk!"
    elif(dict1['Coffee'] < recipe_requirements[choice]['Coffee']):
        return "Sorry there is not enough Coffee!"
    else:
        return "enough resources"
    
def serve(choice, dict1):
    for resource in dict1:
        dict1[resource] -= recipe_requirements[choice][resource]           
    return f"Here is your {choice}☕. Enjoy!"

while machine_is_on:          
    order = input("What would you like? ('espresso'/'latte'/'cappuccino')?: ")
    if order == 'report':
        print_report(resources, money)
    elif order == 'off':
        machine_is_on = False
    else:
        resource_availability = check_resources(order, resources)
        if resource_availability != "enough resources":
            print(resource_availability)
        else:
            payment = pay(order)
            if payment[1] == True:
                print(payment[0])
                print(serve(order, resources))
                money += product_cost[order]
            else:
                print(payment[0])
    

                                    