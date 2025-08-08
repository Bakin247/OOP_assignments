# Parent Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in %
    
    def make_call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")
    
    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%")

# Child Class
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system
    
    def play_game(self, game):
        if self.battery > 10:
            print(f"{self.brand} {self.model} is playing {game} with {self.cooling_system} cooling system!")
            self.battery -= 10
        else:
            print(f"{self.brand} {self.model} battery too low to play games.")

# Creating objects
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 80)
phone2 = GamingSmartphone("Asus", "ROG Phone 7", 512, 90, "Advanced Liquid")

# Using methods
phone1.make_call("Alice")
phone2.play_game("Call of Duty")
phone2.charge(5)
