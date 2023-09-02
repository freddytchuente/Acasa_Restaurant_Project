import json
import os
from pathlib import Path

def get_menu_from_json():
    # Get the menu from JSON
    os.chdir(Path(__file__).parent)
    with open("menu.json", mode= "r", encoding = "UTF-8") as file:
        menu:dict = json.load(file)
    return menu

def show_menu(menu):
    valid_dish_ids: list = []
    for category in menu:
        print(category)
        print("*" * 10)

        for dish in menu[category]:
            print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]} €')
            valid_dish_ids.append(dish["id"])

        print()

    return valid_dish_ids

def get_guest_information():
    # Get the Guest Information
    print("\nGastinfo")
    print("*" * 10)
    first_name: str = input("Vorname: ").strip().title()
    last_name: str = input("Nachname: ").strip().upper()

    return first_name, last_name

def get_guest_wishes(valid_dish_ids):
    # Get the Guest wishes
    print("\nIhre Wünsche")
    print("*" * 10)
    user_wishes: list = []
    while True:
        user_wish: int = int(input("> "))

        # break point
        if user_wish == 0:
            break
        if user_wish not in valid_dish_ids:
            print("Leider bieten wir das nicht")
            continue
        user_wishes.append(user_wish)

    # Sort user wishes
    user_wishes.sort()

    return user_wishes

def build_receipt_text(first_name, last_name, menu, user_wishes):
    receipt_text = f"\nQuittung für {first_name} {last_name}\n"
    receipt_text += "*" * 30 + "\n"
    total: float = 0

    # Search for each user wish id in the whole MENU
    for user_wish_id in user_wishes:
        for category in menu:
            for dish in menu[category]:
                if user_wish_id == dish["id"]:
                    receipt_text += f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€\n'
                    total += dish["price"]

    receipt_text += f"Summe: {round(total, 2)} €\n"
    receipt_text += "Vielen Dank für Ihren Besuch!\n"

    return receipt_text

def save_receipt_to_file(receipt_text):
    # Save receipt to text file
    with open("receipt.txt", mode= "w", encoding= "UTF-8") as file:
        file.write(receipt_text)

def main():
    # 1. Get the menu from JSON
    menu = get_menu_from_json()

    # 2. Greeting
    print("Willkommen bei ACASA Restaurant")
    print("*" * 30)

    # 3. Show the menu
    valid_dish_ids = show_menu(menu)

    # 4. Get the Guest Information
    first_name, last_name = get_guest_information()

    # 5. Get the Guest wishes
    user_wishes = get_guest_wishes(valid_dish_ids)

    # 7. Build Receipt Text
    receipt_text = build_receipt_text(first_name, last_name, menu, user_wishes)

    # 8. Save receipt to text file
    save_receipt_to_file(receipt_text)

    # 9. Print receipt
    print(receipt_text)

if __name__ == "__main__"

