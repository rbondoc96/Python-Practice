from sys import exit
from math import ceil
from time import sleep
from random import randint, randrange

from player import Player
from inventory import InventoryItem

class Game:

    def __init__(self, start_gold=None):
        player_gold = start_gold or randint(500, 6000)

        self.player = Player(
            "Player",
            player_gold,
            randint(5, 100),
        )
        self.merchant = Player(
            "Merchant",
            randint(500, 6000),
            randint(5, 100),
        )

        self.player.add_items(
            InventoryItem("Tabby Cat", randint(1, 50), randint(1, 1000)),
            InventoryItem("Tuxedo Cat", randint(1, 50), randint(1, 1000)),
            InventoryItem("Pembroke Welsh Corgi", randint(1, 50), randint(1, 1000)),
            InventoryItem("French Bulldog", randint(1, 50), randint(1, 1000)),
        )

        self.merchant.add_items(
            InventoryItem("Calico Cat", randint(1, 50), randint(1, 1000)),
            InventoryItem("Raspberry", randint(1, 50), randint(1, 1000)),
            InventoryItem("Dragon Fruit", randint(1, 50), randint(1, 1000)),
            InventoryItem("Gasoline", randint(1, 10), randint(3000, 6000))
        )


    def print_scenario(self, story, choices, delay=1.5, numbered=False):
        for line in story:
            print(line)
            
            if delay:
                sleep(delay)

        print("".center(30, "-"))

        for idx, line in enumerate(choices):
            if numbered:
                print(f"{idx + 1}:", line)
            else:
                print(line)

        print("".center(30, "-"))

        print("Current Gold:", self.player.gold)


    def start(self, restart=False):
        story = [
            "Hi there! Welcome to Phaggot Farms.",
            "What can I do for you today?"
        ]
        story = [story[1]] if restart else story

        choices = [
            "Let's see what you have available.",
            "I have some stuff to sell.",
            "I'm all good, thanks!"
        ]

        self.print_story(story)
        res = self.prompt_choice(choices, ret_num=True)  

        print(res)
        if res == "1":
            self.player_buy()
        elif res == "2":
            self.player_sell()
        elif res == "3":
            self.end("Thank you, have a nice day!")
        else:
            self.end("Hm. Don't know what that is. Bye!")


    def end(self, msg):
        print(msg)
        exit(0)


    def player_buy(self):
        b_pow = self.player.compare_influence(self.merchant)[1]

        story = [
            self.merchant.inventory_to_str(),
            "What would you like to buy?",
            "To go back to the start menu, type q."
        ]

        choices = self.merchant.inventory

        meta = [
            "".center(30, "-"),
            f"Player Influence: {self.player.influence}",
            f"Merchant Influence: {self.merchant.influence}",
            f"Buying Modifier: {b_pow}",
            "".center(30, "-"),
        ]

        self.print_story(story)
        
        item = self.prompt_choice(choices, meta)

        if item is None:
            self.start(restart=True)
            return

        quantity = self.prompt_quantity(item)        
        total_price = ceil(item.price * b_pow) * quantity

        print(f"Final price is {total_price} gold. Proceed with the transaction? Y/N")
        confirmation = input("> ")

        if confirmation in ["n", "N", "no", "No"]:
            self.player_buy()
            return

        if self.player.gold < total_price:
            print("Oops, you don't have enough gold for that!")
            sleep(1)
            self.player_buy()
            return

        print("Total gold spent:", total_price)
        self.player.gold -= total_price
        self.merchant.gold += total_price
        self.merchant.remove_item(item.name, quantity)
        self.player.add_item(item.name, quantity, item.price)
        sleep(1)

        print(f"Thank you! Enjoy your {item.name}!")
        sleep(1)
        self.player_buy()

    
    def player_sell(self):
        s_pow = self.player.compare_influence(self.merchant)[0]

        story = [
            self.player.inventory_to_str(),
            "What would you like to sell?",
            "To go back to the start menu, type q."
        ]

        choices = self.player.inventory

        meta = [
            "".center(30, "-"),
            f"Player Influence: {self.player.influence}",
            f"Merchant Influence: {self.merchant.influence}",
            f"Selling Modifier: {s_pow}",
            "".center(30, "-"),
        ]

        self.print_story(story)
        
        item = self.prompt_choice(choices, meta)

        if item is None:
            self.start(restart=True)
            return

        quantity = self.prompt_quantity(item)        
        total_price = ceil(item.price * s_pow) * quantity

        print(f"Final selling price is {total_price} gold. Proceed with the transaction? Y/N")
        confirmation = input("> ")

        if confirmation in ["n", "N", "no", "No"]:
            self.player_sell()
            return

        if self.merchant.gold < total_price:
            print("Oops, I don't have enough gold for that!")
            print(f"Take {self.merchant.gold} gold for it? Y/N")
            conf = input("> ")

            if conf in ["n", "N", "no", "No"]:
                sleep(1)
                self.player_sell()
                return
            
            total_price = self.merchant.gold

        print("Total gold obtained:", total_price)
        self.merchant.gold -= total_price
        self.player.gold += total_price
        self.player.remove_item(item.name, quantity)
        self.merchant.add_item(item.name, quantity, item.price)
        sleep(1)

        print(f"Wow, thanks for the {item.name}!")
        sleep(1)
        self.player_sell()


    def print_story(self, story, delay=1.5):
        for line in story:
            print(line)

            if delay:
                sleep(delay)


    def prompt_choice(self, choices, meta=None, ret_num=False):
        for idx, line in enumerate(choices):
            print(f"{idx + 1}:", line)

        print("".center(30, "-"))
        print("Player Gold:", self.player.gold)   
        print("Merchant Gold:", self.merchant.gold)

        if meta:
            for line in meta:
                print(line)
        
        choice = input("> ")

        if choice == "q" or choice == "Q":
            return None

        if not choice.isdigit():
            print("Please enter a positive integer.")
            return self.prompt_choice(choices)

        choice = int(choice)
        if choice not in range(1, len(choices) + 1):
            print("That item is not in the range of choices.")
            return self.prompt_choice(choices)

        if ret_num:
            return str(choice)

        return choices[choice - 1]


    def prompt_quantity(self, item):
        print(f"How many {item.name}?")
        quantity = input("> ")
        
        if not quantity.isdigit():
            print("Enter a positive integer.")
            return self.prompt_quantity(item)

        quantity = int(quantity)
        if quantity > item.quantity:
            print("Quantity is too much. Enter a smaller number.")
            return self.prompt_quantity(item)

        return quantity
