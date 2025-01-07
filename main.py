# file: main.py
from process.process import TravelProcess
from view.view import TravelView

def main():
    process = TravelProcess()
    view = TravelView()

    while True:
        print("\n1. Lihat Daftar Travel")
        print("2. Pesan Travel")
        print("3. Lihat Daftar Pemesanan")
        print("4. Keluar")

        try:
            choice = int(input("Pilih menu: "))
            if choice == 1:
                view.display_travels()
            elif choice == 2:
                view.display_travels()
                try:
                    id_travel = int(input("Masukkan ID Travel: "))
                    nama = input("Masukkan nama Anda: ")
                    process.add_order(nama, id_travel)
                    print("Pemesanan berhasil!")
                except ValueError as e:
                    print(f"Input tidak valid: {e}")
            elif choice == 3:
                orders = process.get_orders()
                view.display_orders(orders)
            elif choice == 4:
                print("Terima kasih telah menggunakan layanan kami!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih angka 1-4.")
        except ValueError:
            print("Input harus berupa angka.")

if __name__ == "__main__":
    main()