#PROJECT-SMART VENDING MACHINE
class Item:
    def __init__(self,name,price,code,stock=5):
        self.name = name
        self.price = price
        self.code = code
        self.stock = stock

    def display_item_details(self):
        print(f"Code: {self.code} | Item: {self.name} | price: {self.price} | Stock: {self.stock}")


class vendinMachine:
    def __init__(self):
        self.inventory = []
        self.total_cash = 0
        self.current_balance = 0

    def add_item_to_machine(self,item):
        self.inventory.append(item)

    def show_menu(self):
        print("\n-------VENDING MACHINE MENU--------")
        if not self.inventory:
            print("The machine is empty!")
            return
        for item in self.inventory:
            item.display_item_details()

    def insert_money(self,amount):
        if amount > 0:
            self.current_balance += amount
            print(f"successfully deposited: {amount} Current balance: {self.current_balance}")
        else:
            print("Please insert a vailed amount")

    def buy_product(self,code):
            target_item = None
            for item in self.inventory:
                if item.code.upper() == code.upper():
                    target_item = item
                    break

            if target_item is None:
                print("Invailed code! Please choose a vailed slot")
                return

            if target_item.stock <=0:
                print(f"Sorry, {target_item.name} is out of stock!")
                return

            if self.current_balance < target_item.price:
               print(f"Insufficient funds! {target_item.name} costs {target_item.name} Please deposit more money")
               return

            target_item.stock -=1
            self.total_cash += target_item.price

            change = self.current_balance - target_item.price
            print(f"Dispensing {target_item.name}...Enjoy your sanck!")

            if change > 0:
                print(f"Returning your change: {change}")
            self.current_balance = 0

if __name__ == "__main__":
    vm = vendinMachine()

    chips = Item("Lays chips" , 20 , "A1" , stock=2)
    soda = Item("coca cola" , 40 , "B1" , stock=5)

    vm.add_item_to_machine(chips)
    vm.add_item_to_machine(soda)

    vm.show_menu()

    print("\n------Attempting to buy without money-------")
    vm.buy_product("A1")

    print("\n------Inserting money-------")
    vm.insert_money(50)

    print("\n-------buying Item----------")
    vm.buy_product("A1")

    vm.show_menu()
