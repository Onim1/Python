menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"naem": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order) :
    print ('Calculating bill subtotal...')
    calc_subtotal = 0

    for item in order:
        calc_subtotal += item["price"]
    return round(calc_subtotal, 2)


def calculate_tax(*subtotal) :
    print('Calcutating bill tax from subtotal...')
    tax = round(subtotal * 0.15, 2)
    return tax

def summarize_order(order) :
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    names = [item["name"] for item in order]

    return names, total


def print_order(order) :
    print('you have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

def display_menu() :
    print("-------- Menu ----------")
    for selection in menu :
        print(f"{selection}. {menu[selection]['name'] : < 9} | {menu[selection]['price'] : > 5}")
    print()

def take_order() :
    display_menu()
    order = []
    count = 1
    for i in range(3):
        while True:
            try:
                item = int(input(f'select menu item number {count} (from 1 tto 5): '))
                if item in menu:
                    order.append(menu[item])
                    count += 1
                    break
                else:
                    print("Please select a valid menu item number (i to 5).")
            except ValueError:
                print("Please entr a valid number.")
    return order

def main() :
    order = take_order()
    print_order(order)

    subtotal = calculate_subtotal(order)
    print("subtotal for the order is: $" + str(subtotal))

    tax = calculate_tax(subtotal)
    print("Tax for the order in: $" + str(tax))

    names, total = summarize_order(order)
    print("Names of items ordered:", names)
    print("total for the order is: $" + str(total))

if __name__ == "__name__":
    main
import random
f = open("pername.txt", "r")
f_contant = f.read()
#print(f_contant)
f_contant_list = f_contant.split("\n")
f.close()
print(random.choice(f_contant_list))
