# file: data/data.py

class Travel:
    def __init__(self, id_travel, travel, destination, price):
        self.id_travel = id_travel
        self.travel = travel
        self.destination = destination
        self.price = price

    def __str__(self):
        return f"{self.id_travel}. {self.destination} - Rp{self.price}"

# Corrected travel_list with all arguments provided
travel_list = [
    Travel(1, "Bali", "Bali", 500000),
    Travel(2, "Yogyakarta", "Yogyakarta", 300000),
    Travel(3, "Lombok", "Lombok", 400000),
]
