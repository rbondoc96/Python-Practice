class InventoryItem:

    def __init__(self, name, quantity, price=None):
        self.name = name.title()
        self.quantity = quantity        
        self.price = price


    def __str__(self):
        return self.name


    def decrement(self, dec=1):
        self.quantity -= max(0, dec)


    def increment(self, inc=1):
        self.quantity += max(0, inc)


    def change_price(self, price):
        self.price = price


class Inventory:

    def __init__(self):
        self.stock = []


    def __str__(self):
        buffer = []

        for item in self.stock:
            buffer.append(str(item))
        
        return "\n".join(buffer)


    def __len__(self):
        return len(self.stock)


    def __getitem__(self, i):
        return self.stock[i]


    def __getslice__(self, i, j):
        return self.stock[i, j]


    def inventory(self):
        """Generator that yields each item in the Inventory
        """
        for item in self.stock:
            yield item


    def remove_items(self, *items):
        for item in items:
            self.remove(item.name, item.quantity)


    def remove(self, name, count=1):
        """Remove an item that's in stock. Removes 1 by default.
        Raises a ValueError if removing an item that doesn't exist."""
        idx = self.index_of(name)

        if idx <= -1:
            raise ValueError(f"Item {name} is not in the inventory.")
        
        item = self.stock[idx]

        if count == item.quantity:
            self.stock.remove(item)
            self.stock.sort(key = lambda elem: elem.price)
        elif count < item.quantity:
            item.decrement(count)
        else:
            raise ValueError("Count is greater than the item's quantity")


    def add_items(self, *items):
        """Add a list of InventoryItems to the stock.
        Changes an existing item's price if the new price is different.
        Changes price to 0 if new price < 0"""

        for item in items:
            self.add(item.name, item.quantity, item.price)
  

    def add(self, name, quantity, price=None):  
        """Add an item to the inventory stock.
        Changes an existing item's price.
        If given price < 0, price is set to 0."""

        idx = self.index_of(name)

        if price and price < 0:
            price = 0

        if idx <= -1:
            self.stock.append(
                InventoryItem(name.title(), quantity, price)
            )
            self.stock.sort(key = lambda elem: elem.price)
        else:
            item = self.stock[idx]
            item.increment(quantity)

            if price is not None:
                item.change_price(price)


    def index_of(self, name):
        """Returns index of the first instance of an item if it's in 
        stock, or -1"""

        for idx, elem in enumerate(self.stock):
            if elem.name == name.title():
                return idx

        return -1


    def get_item(self, name):
        idx = self.index_of(name)

        return self.stock[idx] if idx >= 0 else None


def test_me():
    inventory = Inventory()

    inventory.add("Apples", 10, -10)
    inventory.add("Apples", 10, 20)
    inventory.add("Apples", 10, -10)
    inventory.add("Apples", 10, 20)
    inventory.add("Oranges", 5, 60)
    inventory.add("Oranges", 1, 60)
    inventory.add("Apples", 5, 70)

    inventory.add_items(
        InventoryItem("Apples", 10),
        InventoryItem("Oranges", 7)
    )

    inventory.remove("Apples", 24)

    inventory.remove_items(
        InventoryItem("Oranges", 3),
        InventoryItem("Apples", 1)
    )

    print(inventory)


if __name__ == "__main__":
    test_me()