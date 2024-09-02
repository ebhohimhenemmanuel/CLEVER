class Computer:
    def __init__(self, max_price):
        self.__max_price = max_price

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price

# Create an object for the class Computer
computer = Computer(1000)

# Display the initial selling price
computer.sell()

# Change the value of max price
computer.set_max_price(1200)

# Display the updated selling price
computer.sell()
