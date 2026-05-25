import sqlite3


# CONNECT TO DATABASE

connection = sqlite3.connect("grocery.db")
cursor = connection.cursor()


# CREATING THE TABLE UNLESS TABLE ALREADY EXISTS

cursor.execute("""
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    cheapest_item_producer TEXT NOT NULL,
    price_nzd REAL NOT NULL CHECK(price_nzd >= 0)
)
""")


# TELLING THE CODE WHAT THE DATA IS

items_data = [
    (1, 'Milk cartons', 'dairy', 'The Warehouse', 4.5),
    (2, 'Eggs 12pk', 'dairy', "PAK'nSAVE", 10.5),
    (3, 'Block of cheese', 'dairy', "PAK'nSAVE", 6),
    (4, 'Wheat bread', 'bakery', 'Woolworths', 3.5),
    (5, 'Bananas', 'produce', 'Asian Food Mart', 3),
    (6, 'Lettuce', 'produce', 'Asian Food Mart', 3.99),
    (7, 'Potatoes', 'produce', 'Asian Food Mart', 4.5),
    (8, 'Carrots', 'produce', 'Woolworths', 2.5),
    (9, 'Apples', 'produce', 'Woolworths', 4),
    (10, 'Pasta noodles', 'pantry', 'Woolworths', 3),
    (11, 'Shin ramen', 'pantry', "PAK'nSAVE", 2),
    (12, 'Weet-bix', 'pantry', "PAK'nSAVE", 8),
    (13, 'Ground beef', 'meat', "PAK'nSAVE", 18),
    (14, 'Chicken breast', 'meat', "PAK'nSAVE", 15),
    (15, 'Potato chips', 'pantry', "PAK'nSAVE", 3),
    (16, 'Coke', 'beverages', 'Four Square', 3.5),
    (17, 'Spirit', 'beverages', 'Four Square', 3.5),
    (18, 'Toilet paper', 'household', "PAK'nSAVE", 9),
    (19, 'Coffee beans', 'pantry', "PAK'nSAVE", 8),
    (20, 'Canned tuna', 'meat', "PAK'nSAVE", 3)
]
# PUTS ALL OF THE DATA INTO A DATABASE TABLE!

cursor.executemany("""
INSERT OR IGNORE INTO items
VALUES (?, ?, ?, ?, ?)
""", items_data)

connection.commit()


# PRINTING INSTRUCTIONS

print("\n==============================")
print("GROCERY SEARCH SYSTEM")
print("==============================")
print("Type an item to search.")
print("OR type 'exit' to quit the program.")
print("==============================\n")


# SHOWing item list 

print("Available items:\n")

cursor.execute("SELECT name FROM items")
all_items = cursor.fetchall()

for item in all_items:
    print("-", item[0])


# INFINITE LOOP!

while True:

    search_item = input("\nEnter item to search (or type 'exit'): ")

    # EXIT CODEEE
    if search_item.lower() == "exit":
        print("\nGoodbye 👋")
        break

#SQL CODE THINGY
    cursor.execute("""
    SELECT * FROM items
    WHERE LOWER(name) LIKE LOWER(?)
    """, ('%' + search_item + '%',))

    results = cursor.fetchall()

    print("\n---------------------------")

# PRINTING OUT THE RESULTSSSSS/ THE DATA ASKED
    if results:
        print("Item found:\n")

        for item in results:
            print(f"ID: {item[0]}")
            print(f"Name: {item[1]}")
            print(f"Category: {item[2]}")
            print(f"Cheapest Store: {item[3]}")
            print(f"Price (NZD): ${item[4]}")
            print("---------------------------")
    else:
        print("Sorry, we cannot find that item anywhere.")


# CLOSE THE DATABASE

connection.close()