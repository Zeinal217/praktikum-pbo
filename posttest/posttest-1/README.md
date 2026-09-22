# Documentation README.md

# Sistem Manajemen Laundry "CleanWash" (Python OOP)

Sistem Manajemen Laundry **CleanWash** adalah aplikasi berbasis teks yang dirancang menggunakan alur Pemrograman Berorientasi Objek (Object-Oriented Programming / OOP) dalam bahasa Python. Aplikasi ini memfasilitasi pengelolaan jenis layanan laundry, data pelanggan beserta deposit saldo, pencatatan transaksi, perhitungan diskon otomatis, serta cetak nota transaksi.

---

## 1. Arsitektur & Struktur Class

Program ini dibangun oleh **3 Class Utama** yang saling berinteraksi:

### A. `LayananLaundry`
Mengelola informasi katalog layanan laundry dan kalkulasi estimasi waktu pengerjaan.
- **Atribut Kelas:** `nama_instansi` (Nama identitas bisnis laundry).
- **Atribut Encapsulated (Private):** `__tarif_per_kg` (Menggunakan `@property` & `@setter` dengan validasi nilai > 0).
- **Method:**
  - `info_layanan()` (Instance Method): Mengembalikan string perincian layanan.
  - `dari_dict(cls, data)` (Class Method): Factory method untuk menginstansiasi objek dari tipe dictionary.
  - `hitung_estimasi_selesai(estimasi_hari)` (Static Method): Menghitung waktu penyelesaian laundry berbasis `datetime`.

### B. `Pelanggan`
Mengelola profil identitas pelanggan dan saldo deposit pembayaran.
- **Atribut Kelas:** `diskon_member` (Rasio persentase diskon potongan harga global).
- **Atribut Encapsulated (Private):** `__saldo` (Menggunakan `@property` & `@setter` dengan validasi nilai >= 0).
- **Method:**
  - `tambah_saldo(nominal)` & `kurangi_saldo(nominal)` (Instance Method): Mengelola transaksi deposit saldo pelanggan.
  - `ubah_diskon_member(cls, persen_baru)` (Class Method): Mengubah besaran diskon member global.
  - `validasi_no_telp(no_telp)` (Static Method): Memeriksa keabsahan format nomor telepon pelanggan.

### C. `Transaksi`
Menjadi *orchestrator* yang menghubungkan objek `Pelanggan` dan `LayananLaundry` untuk memproses pesanan dan pembayaran.
- **Atribut Kelas:** `total_transaksi` (Penghitung otomatis jumlah transaksi yang diinstansiasi).
- **Atribut Encapsulated (Private):** `__berat_kg`, `__status_pembayaran`, `__total_harga`.
- **Method:**
  - `proses_pembayaran_saldo()` & `bayar_tunai(jumlah_uang)` (Instance Method): Memproses pelunasan transaksi.
  - `cetak_nota()` (Instance Method): Menampilkan nota transaksi ke konsol.
  - `reset_counter_transaksi(cls)` (Class Method): Mereset penghitung jumlah transaksi kelas.
  - `format_rupiah(nominal)` (Static Method): Menerapkan formatting standar mata uang Rupiah.