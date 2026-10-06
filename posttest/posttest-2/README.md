# Sistem Manajemen Laundry CleanWash

## 1. Deskripsi Program
CleanWash adalah sebuah sistem informasi manajemen operasional laundry berbasis teks. Sistem ini dirancang untuk mengelola berbagai entitas bisnis secara terpadu, mulai dari katalog layanan, basis data pelanggan, penempatan karyawan di cabang, hingga pencatatan transaksi dan item cucian.

## 2. Penerapan Relasi UML (Class Relationships)
Sistem ini mengimplementasikan tiga tingkat relasi antar objek:

*   **Asosiasi (Hubungan Lemah)**
    Asosiasi terjadi antara entitas `Karyawan` dan `Pelanggan`. Pada method `layani_pelanggan(self, pelanggan)` di dalam class `Karyawan`, objek `Pelanggan` hanya dikirim sebagai parameter sementara untuk kebutuhan eksekusi fungsi tersebut. Class `Karyawan` tidak menyimpan referensi objek pelanggan secara permanen (tidak ada deklarasi variabel seperti `self.pelanggan = pelanggan`), sehingga kedua objek tetap independen.
*   **Agregasi (Hubungan Sedang)**
    Agregasi diimplementasikan pada class `CabangLaundry` yang bertindak sebagai wadah bagi sekumpulan objek `Karyawan`. Objek `Karyawan` diinstansiasi secara mandiri di lingkup luar, lalu dimasukkan ke dalam penampung `_karyawan` melalui method `tambah_karyawan`. Karena referensi objek berasal dari luar, siklus hidup karyawan tidak terikat pada eksistensi cabang; jika entitas `CabangLaundry` dihapus, data karyawan tetap eksis di memori.
*   **Komposisi (Hubungan Kuat)**
    Komposisi terlihat pada relasi antara class `Transaksi` dan `ItemCucian`. Objek `ItemCucian` secara eksklusif dibuat (diinstansiasi) tepat di dalam method `tambah_item` milik `Transaksi`. Melalui pendekatan ini, siklus hidup item cucian bergantung penuh pada transaksi induknya. Jika sebuah instance transaksi dihapus dari sistem, seluruh objek item cucian di dalamnya akan ikut musnah karena tidak ada referensi independen di luarnya.

## 3. Penerapan Inheritance (Pewarisan)
Variasi operasional layanan laundry dalam sistem ini dikelola menggunakan prinsip pewarisan:

*   **Superclass & Subclass**
    Class `LayananLaundry` bertindak sebagai *Parent Class* (Superclass) yang membungkus properti fundamental dari sebuah layanan (ID, nama, estimasi hari, tarif dasar). Class `LayananReguler` dan `LayananExpress` difungsikan sebagai *Child Class* (Subclass) yang secara langsung mewarisi sifat dasar tersebut sembari mengimplementasikan perilaku spesifik.
*   **Penggunaan Hak Akses Protected**
    Atribut tarif pada parent class dideklarasikan menggunakan tingkat akses protected (`_tarif_per_kg`) alih-alih private murni (`__tarif_per_kg`). Modifikasi visibilitas ini krusial secara logika arsitektur, karena memungkinkan class turunannya (subclass) untuk membaca dan memanipulasi perhitungan tarif tanpa terhalang batasan *name mangling* dari bahasa Python.
*   **Penggunaan super() & Atribut Unik**
    Setiap subclass memanggil `super().__init__(...)` pada konstruktor utamanya guna mendelegasikan inisialisasi state dasar ke *parent class*. Setelah fondasi objek terkonstruksi, masing-masing subclass mendeklarasikan atribut uniknya: atribut `jenis_pewangi` ditambahkan ke `LayananReguler`, dan atribut `biaya_tambahan` pada `LayananExpress`.
*   **Method Overriding**
    Untuk mengakomodasi perbedaan kebutuhan format keluaran dan perhitungan, method `info_layanan()` milik parent class ditimpa ulang (*di-override*) pada masing-masing subclass. `LayananReguler` memodifikasi pengembalian *string* dengan menyisipkan detail pewangi, sementara `LayananExpress` melangkah lebih jauh dengan menyertakan operasi matematis yang menjumlahkan `_tarif_per_kg` dengan `biaya_tambahan` sebelum merender totalnya ke layar.