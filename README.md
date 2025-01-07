# PROJECT-UAS
Pendahuluan   
Program pemesanan tiket travel wisata ini dirancang untuk mengelola proses pemesanan tiket dengan memanfaatkan konsep Pemrograman Berorientasi Objek (OOP) dan struktur modular.    
Program ini memungkinkan pengguna untuk melihat daftar destinasi, pemesanan tiket, dan melihat daftar harga yang telah dilakukan.   

Struktur Program   
Program ini terdiri dari tiga komponen utama yang terorganisir dalam folder sesuai dengan fungsinya:   

Folder data   
Berisi data destinasi yang tersedia untuk dipesan. Data ini disimpan sebagai daftar objek yang merepresentasikan setiap tiket dengan atribut seperti ID, nama, dan harga.   

Folder process   
Mengelola logika utama untuk memproses pemesanan. Misalnya, melakukan validasi input pengguna, memastikan ketersediaan tiket, dan mencatat pesanan.   

Folder view   
Bertanggung jawab untuk menampilkan informasi ke pengguna, seperti daftar destinasi yang tersedia dan daftar pesanan.    

File main.py   
Berfungsi sebagai titik masuk program. File ini mengatur interaksi antara modul data, process, dan view.   

Fitur Program   
Lihat Daftar destinasi
Program menampilkan daftar destinasi yang tersedia, termasuk ID, tempat destinasi, dan harga tiketnya. Daftar ini diambil dari modul data.   

pemesanan tiket
Pengguna dapat memesan tiket dengan memasukkan nama dan ID destinasi.   

Program akan memvalidasi nama untuk memastikan tidak kosong.   
Program juga memvalidasi ID destinasi untuk memastikan bahwa destinasi yang dipilih ada dalam daftar.   
Jika validasi berhasil, data pesanan disimpan dalam sistem.   
Lihat Daftar Pesanan
Program menampilkan semua pesanan yang telah dilakukan. Setiap tiket pemesanan mencakup nama pemesan, tiket yang di pesan, dan harga tiketnya. Jika belum ada pesanan, program akan menampilkan pesan bahwa belum ada data.   

Konsep yang Digunakan   
Pemrograman Berorientasi Objek (OOP)   
Program menggunakan class untuk memodelkan data dan logika, seperti:   

Class destination untuk merepresentasikan data destinasi.   
Class travelsProcess untuk mengelola logika pemesanan.   
Class travelsView untuk menampilkan data.   
Modularitas   
Program dipisahkan menjadi beberapa modul agar lebih terstruktur dan mudah dipelihara.   

Validasi Input dan Error Handling   

Input pengguna divalidasi untuk mencegah kesalahan, seperti nama kosong atau ID destinasi yang tidak valid.   
Error handling dilakukan dengan pesan yang informatif agar pengguna tahu apa yang salah.   
Alur Program   
Program dimulai dengan menampilkan menu utama, yang memiliki 4 pilihan:   

Melihat daftar destinasi yang tersedia.   
Memesan tiket.   
Melihat daftar pemesanan.   
Keluar dari program.   
Pengguna memilih salah satu opsi:   

Jika memilih "Lihat Daftar destinasi", program akan menampilkan semua destinasi.    
Jika memilih "pesan tiket", pengguna akan diminta untuk memasukkan ID destinasi dan nama. Setelah itu, program akan memvalidasi input dan mencatat pemesanan jika valid.   
Jika memilih "Lihat Daftar Pesanan", program akan menampilkan daftar pesanan yang sudah dilakukan.   
Program terus berjalan sampai pengguna memilih "Keluar".  

# program Output    
![Gambar1](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135258.png?raw=true)  
![Gambar2](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135316.png?raw=true)   
![Gambar3](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135353.png?raw=true)   
![Gambar4](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135405.png?raw=true)   
![Gambar5](https://github.com/Raffxzx/PROJECT-UAS/blob/main/ss/Screenshot%202025-01-06%20135413.png?raw=true)   
   
