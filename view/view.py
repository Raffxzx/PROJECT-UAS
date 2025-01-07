# file: view/view.py
from data.data import travel_list

class TravelView:
    def display_travels(self):
        print("\nDaftar Travel:")
        for travel in travel_list:
            print(travel)

    def display_orders(self, orders):
        print("nDaftar Pemesanan:")
        if not orders:
            print("Belum ada pemesanan.")
        else:
            for nama, travel in orders.items():
                print(f"{nama}memesan {travel}")