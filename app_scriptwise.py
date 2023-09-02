import json
import os
from pathlib import Path
os.chdir(Path(__file__).parent)

menu = {
    "Pizzen": [
    {"id": 100, "title": "Pizza Margeritta", "price": 12},
    {"id": 101, "title": "Pizza Tunfisch", "price": 12},
    {"id": 102, "title": "Pizza Fungi", "price": 12}
    ],

    "Aufläufe": [
    {"id": 200, "title": "Auflauf Nudeln", "price": 10},
    {"id": 201, "title": "Auflauf Katoffeln", "price": 10}
    ],

    "Salat": [
    {"id": 300, "title": "Salat Normal", "price": 10},
    {"id": 301, "title": "Salat Kaiser", "price": 10}
    ]
}

valid_dish_ids: list = [] # The ids of all dishes
user_wishes: list = [] # user wishes [ids]
receipt_text: str = "" # The text of the receipt
total: float = 0 #the total of receipt which the customer should pay

# 1. Get the menu from JSON
#~~~~~~~~~~~~~~~~~~~~~~~~~~
with open("menu.json", mode= "r", encoding = "UTF-8") as file:
    menu:dict = json.load(file)

# 2. Greeting
#~~~~~~~~~~~~

print("Willkommen bei ACASA Restaurant")
print("*" * 30)

# 3. Show the menu
#~~~~~~~~~~~~~~~~~
for category in menu:
    print(category)
    print("*" * 10)

    for dish in menu[category]:
        print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]} €')
            
        valid_dish_ids.append(dish["id"])

    print()
              
# 4. Get the Guest Information
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("\nGastinfo")
print("*" * 10)
first_name: str = input("Vorname: ").strip().title()
last_name: str = input("Nachname: ").strip().upper()

# 5. Get the Guest wishes
#~~~~~~~~~~~~~~~~~~~~~~~~
print("\nIhre Wünsche")
print("*" * 10)
while True:
    user_wish: int = int(input("> "))

# break point
    if user_wish == 0:
        break
    if user_wish not in valid_dish_ids:
        print("Leider bieten wir das nicht")
        continue
    user_wishes.append(user_wish)

# 6. Sort user wishes
#~~~~~~~~~~~~~~~~~~~~
user_wishes.sort()

#7. Build Receipt Text
#~~~~~~~~~~~~~~~~~~~~~
receipt_txt = f"\nQuittung für {first_name} {last_name}\n"
receipt_text += "*" * 30 + "\n"

# Search  for each user wish id in the whole MENU
for user_wish_id in user_wishes: # [100, 101, 102]
    for category in menu:
        for dish in menu[category]:
            if user_wish_id == dish["id"]:
                receipt_text += f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€\n'
                total += dish["price"]

receipt_text += f"Summe: {round(total, 2)} €\n"

receipt_text += "Vielen Dank für Ihren Besuch!\n"


#8. Save receipt to text file
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~
with open("receipt.txt", mode= "w", encoding= "UTF-8") as file:
    file.write(receipt_text)

#9. Save the receipt
#~~~~~~~~~~~~~~~~~~~
print(receipt_text)
 