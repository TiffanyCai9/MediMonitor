from medications import (
    get_medication, 
    check_expirations, 
    display_inventory, 
    delete_medication, 
    manage_expiry_bin, 
    manage_sale_bin
    )
from db import database_setup

def main():
    print("Welcome to the Pharmacy Expiry Tracker!")
    database_setup()
    
    # Displays menu options
    while True:
        print("\n1. Add a new product")
        print("2. Delete a product")
        print("3. Check for soon-to-be expired products")
        print("4. Check expiry bin")
        print("5. Check sales bin")
        print("6. View inventory")
        print("7. Exit")

        option = input("Choose an option (1 - 7): ")
        if option == '1':
            get_medication()
        elif option == '2':
            delete_medication()
        elif option == '3':
            check_expirations()
        elif option == '4':
            manage_expiry_bin()
        elif option == '5':
            manage_sale_bin()
        elif option == '6':
            display_inventory()
        elif option == '7':
            print("Exiting expiry tracker. See you next time!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 7.")  
        
if __name__ == "__main__":
    main()