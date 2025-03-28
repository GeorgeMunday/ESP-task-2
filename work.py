houses = [['LONDON', 'Terraced', 3, 735000], ['CARDIFF', 'Semi-Detached', 2, 100000], 
          ['LEEDS', 'Terraced', 3, 245000], ['LONDON', 'Semi-Detached', 1, 240000]]
# needed to add commas here and formatted it correctly
sales = []
#ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    they are not used yet
#property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED'] they are not used

def input_val():
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input!")
    
def add_new_property():
    print("new function")

def return_stock():
    print("CURRENT HOUSES FOR SALE \n\n REGION - HOUSE TYPE - BEDROOMS - COST")
    for i in houses:
        print (*i)

def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    for x in existing_regions:
        if x not in unique_list:       
            unique_list.append(x)
    print(*unique_list)

def region_search():
    print("Available Regions")
    unique_regions()
    r_check = False

    while not r_check:
        region_select= input("Please enter region: ").capitalize()

        for x in houses:
            if region_select.upper() == x[0]:
                r_check = True
                if x[0] == region_select.upper():
                    print(x)

        if r_check == False:
            print("Entered region is not valid")



def show_sales():
    if len(sales) > 0:    
        print("Forename  Surname Property cost  Total")
        for i in sales:
            print(*i)
    else:
        print('no sales')


def house_sale():
    sale = []
    customer_forename = input('Please enter customer forename: ')
    customer_surname = input('Please enter customer surname: ')

    # Display house listings better
    for i, item in enumerate(houses, 1):
        print(i, item)

    while True:
        try:
            select = int(input(f'Please select a property (1 to {len(houses)}): '))
            if 1 <= select <= len(houses):
                break
            else:
                print(f"Please select a valid property number between 1 and {len(houses)}.")
        except ValueError:
            print("ERROR: Please enter a valid number.")


    property_selected = houses[select - 1]
    if property_selected not in houses:
        print("This property has already been sold!")
        return

    sub_total = property_selected[3]
    total_fees = 0

    if sub_total > 100000:
        total_fees += 3000 + (sub_total - 100000) * 0.2
    else:
        total_fees += sub_total * 0.3

    final_total = sub_total + total_fees
    sale.append(customer_forename)
    sale.append(customer_surname)
    sale.append(sub_total)
    sale.append(final_total)
    sales.append(sale)

    print(f'Customer Receipt\n\n FORENAME: {sales[-1][0]}  SURNAME: {sales[-1][1]}  PROPERTY COST: {sales[-1][2]}  WITH STAMP DUTY: {sales[-1][3]}')
    print('\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n')
    print(property_selected)
    del houses[select - 1]


while True:
    print(" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n"
                              " 1: View current houses on market \n 2: Search for available houses in a region \n 3: Record"
                              " a sale \n 4: Add a new property for sale \n 5: Show Sales \n 6: Exit")
    menuselection = input_val()

    options = {
        1: return_stock,
        2: region_search,
        3: house_sale,
        4: add_new_property,
        5: show_sales,
        6: exit,
    }
    
    options[menuselection]()