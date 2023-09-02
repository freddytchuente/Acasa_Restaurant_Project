import json
from pathlib import Path


class Restaurant:
    def __init__(self):
        self.valid_dish_ids = []
        self.user_wishes = []
        self.receipt_text = ""
        self.total = 0
        self.menu = {}
        self.first_name = ""
        self.last_name = ""

    def get_menu(self):
        with open("menu.json", mode="r", encoding="UTF-8") as file:
            self.menu = json.load(file)

    def greet_guest(self):
        print("Willkommen bei ACASA Restaurant")
        print("*" * 30)

    def show_menu(self):
        for category in self.menu:
            print(category)
            print("*" * 10)

            for dish in self.menu[category]:
                print(f'{dish["id"]}. {dish["title"]}\t{dish["price"]} €')

                self.valid_dish_ids.append(dish["id"])

            print()

    def get_guest_info(self):
        print("\nGastinfo")
        print("*" * 10)
        self.first_name = input("Vorname: ").strip().title()
        self.last_name = input("Nachname: ").strip().upper()

    def get_guest_wishes(self):
        print("\nIhre Wünsche")
        print("*" * 10)
        while True:
            user_wish = int(input("> "))

            if user_wish == 0:
                break
            if user_wish not in self.valid_dish_ids:
                print("Leider bieten wir das nicht")
                continue
            self.user_wishes.append(user_wish)

    def sort_guest_wishes(self):
        self.user_wishes.sort()

    def build_receipt_text(self):
        self.receipt_text = f"\nQuittung für {self.first_name} {self.last_name}\n"
        self.receipt_text += "*" * 30 + "\n"

        for user_wish_id in self.user_wishes:
            for category in self.menu:
                for dish in self.menu[category]:
                    if user_wish_id == dish["id"]:
                        self.receipt_text += f'{dish["id"]}. {dish["title"]}\t{dish["price"]}€\n'
                        self.total += dish["price"]

        self.receipt_text += f"Summe: {round(self.total, 2)} €\n"
        self.receipt_text += "Vielen Dank für Ihren Besuch!\n"

    def save_receipt_to_text_file(self):
        with open("receipt.txt", mode="w", encoding="UTF-8") as file:
            file.write(self.receipt_text)

    def save_receipt(self):
        print(self.receipt_text)


if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    restaurant = Restaurant()

    restaurant.get_menu()
    restaurant.greet_guest()
    restaurant.show_menu()
    restaurant.get_guest_info()
    restaurant.get_guest_wishes()
    restaurant.sort_guest_wishes()
    restaurant.build_receipt_text()
    restaurant.save_receipt_to_text_file()
    restaurant.save_receipt()
