# PROJECT-UAS
Pendahuluan   
Program penyewaan mobil ini dirancang untuk mengelola proses penyewaan mobil dengan memanfaatkan konsep Pemrograman Berorientasi Objek (OOP) dan struktur modular.    
Program ini memungkinkan pengguna untuk melihat daftar mobil, menyewa mobil, dan melihat daftar penyewaan yang telah dilakukan.   

Struktur Program   
Program ini terdiri dari tiga komponen utama yang terorganisir dalam folder sesuai dengan fungsinya:   

Folder data   
Berisi data mobil yang tersedia untuk disewa. Data ini disimpan sebagai daftar objek yang merepresentasikan setiap mobil dengan atribut seperti ID, nama, dan harga.   

Folder process   
Mengelola logika utama untuk memproses penyewaan. Misalnya, melakukan validasi input pengguna, memastikan ketersediaan mobil, dan mencatat penyewaan.   

Folder view   
Bertanggung jawab untuk menampilkan informasi ke pengguna, seperti daftar mobil yang tersedia dan daftar penyewaan.    

File main.py   
Berfungsi sebagai titik masuk program. File ini mengatur interaksi antara modul data, process, dan view.   

Fitur Program   
Lihat Daftar Mobil   
Program menampilkan daftar mobil yang tersedia, termasuk ID, nama mobil, dan harga sewanya. Daftar ini diambil dari modul data.   

Sewa Mobil   
Pengguna dapat menyewa mobil dengan memasukkan nama dan ID mobil.   

Program akan memvalidasi nama untuk memastikan tidak kosong.   
Program juga memvalidasi ID mobil untuk memastikan bahwa mobil yang dipilih ada dalam daftar.   
Jika validasi berhasil, data penyewaan disimpan dalam sistem.   
Lihat Daftar Penyewaan   
Program menampilkan semua penyewaan yang telah dilakukan. Setiap penyewaan mencakup nama penyewa, mobil yang disewa, dan harga sewanya. Jika belum ada penyewaan, program akan menampilkan pesan bahwa belum ada data.   

Konsep yang Digunakan   
Pemrograman Berorientasi Objek (OOP)   
Program menggunakan class untuk memodelkan data dan logika, seperti:   

Class Car untuk merepresentasikan data mobil.   
Class CarRentalProcess untuk mengelola logika penyewaan.   
Class CarRentalView untuk menampilkan data.   
Modularitas   
Program dipisahkan menjadi beberapa modul agar lebih terstruktur dan mudah dipelihara.   

Validasi Input dan Error Handling   

Input pengguna divalidasi untuk mencegah kesalahan, seperti nama kosong atau ID mobil yang tidak valid.   
Error handling dilakukan dengan pesan yang informatif agar pengguna tahu apa yang salah.   
Alur Program   
Program dimulai dengan menampilkan menu utama, yang memiliki 4 pilihan:   

Melihat daftar mobil.   
Menyewa mobil.   
Melihat daftar penyewaan.   
Keluar dari program.   
Pengguna memilih salah satu opsi:   

Jika memilih "Lihat Daftar Mobil", program akan menampilkan semua mobil.    
Jika memilih "Sewa Mobil", pengguna akan diminta untuk memasukkan ID mobil dan nama. Setelah itu, program akan memvalidasi input dan mencatat penyewaan jika valid.   
Jika memilih "Lihat Daftar Penyewaan", program akan menampilkan daftar penyewaan yang sudah dilakukan.   
Program terus berjalan sampai pengguna memilih "Keluar".  

# program Output    
![Gambar1](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135258.png?raw=true)  
![Gambar2](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135316.png?raw=true)   
![Gambar3](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135353.png?raw=true)   
![Gambar4](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135405.png?raw=true)   
![Gambar5](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135413.png?raw=true)   
   
