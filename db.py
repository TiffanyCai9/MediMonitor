import sqlite3

def database_setup():
    connection = sqlite3.connect('pharmacy_inventory.db')
    cursor = connection.cursor()

    # Medication table
    cursor.execute( '''
        CREATE TABLE IF NOT EXISTS medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ndc TEXT NOT NULL,
            med_type TEXT NOT NULL,
            expiry_date TEXT NOT NULL
            )''')

    # Expired medication table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expired_medications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ndc TEXT NOT NULL,
            med_type TEXT NOT NULL,
            expiry_date TEXT NOT NULL
            )''')

    # OTC sales table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS otc_sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            ndc TEXT NOT NULL,
            expiry_date TEXT NOT NULL
            )''')

    connection.commit()
    connection.close()

        
