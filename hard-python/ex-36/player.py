from inventory import Inventory, InventoryItem


class Player:

    def __init__(self, name, gold, influence):
        self.name = name
        self.gold = gold
        self.influence = influence
        self.inventory = Inventory()


    def __str__(self):
        items = [
            f"{inv.quantity}".ljust(10) + \
            f"{inv.name}".ljust(20) + \
            f"{inv.price}"
        for inv in self.inventory.inventory()]

        return f" {self.name} ".center(36, "=") + \
        f"\nInfluence: {self.influence}"  + \
        f"\nCurrent Gold: {self.gold}" + \
        f"\n\n" + \
        f" Inventory ".center(36, "-") + "\n" + \
        "#".ljust(10) + "Item".ljust(20) + "Price" + "\n" + \
        "".center(36, "-") + \
        f"\n" + "\n".join(items) + "\n"


    def inventory_to_str(self):
        items = [
            f"{inv.quantity}".ljust(10) + \
            f"{inv.name}".ljust(20) + \
            f"{inv.price}"
        for inv in self.inventory.inventory()]

        return "\n" + f" {self.name}'s Inventory ".center(36, "-") + "\n" + \
        "#".ljust(10) + "Item".ljust(20) + "Price" + "\n" + \
        "".center(36, "-") + \
        f"\n" + "\n".join(items) + "\n"


    def compare_influence(self, merchant):
        """Returns modifiers that influence a player's prices when
        buying and selling."""
        diff = self.influence - merchant.influence
        s_pow = 0
        b_pow = 0

        if diff == 0:
            s_pow = b_pow = 1
        else:
            s_pow = (100 + diff) / 100
            b_pow = (100 - diff) / 100

        return (s_pow, b_pow)


    def add_gold(self, gold):
        self.gold += gold


    def subtract_gold(self, gold):
        self.gold -= gold


    def remove_items(self, *items):
        self.inventory.remove_items(*items)


    def remove_item(self, name, count):
        self.inventory.remove(name, count)


    def add_items(self, *items):
        self.inventory.add_items(*items)


    def add_item(self, name, count, price):
        self.inventory.add(name, count, price)