# file: process/process.py
from data.data import travel_list

class TravelProcess:
    def __init__(self):  # Corrected method name
        self.orders = {}  # Dictionary to store bookings {name: Travel}

    def add_order(self, nama, id_travel):
        # Validate Travel ID
        travel = next((t for t in travel_list if t.id_travel == id_travel), None)
        if travel:
            if nama not in self.orders:  # Check if the name already exists in the orders
                self.orders[nama] = travel
            else:
                raise ValueError(f"Pelanggan {nama} sudah memesan travel.")
        else:
            raise ValueError("ID Travel tidak valid.")

    def get_orders(self):
        return self.orders
