Sistem Manajemen Laundry "CleanWash" 

Sistem Manajemen Laundry "CleanWash" adalah aplikasi berbasis teks yang dirancang menggunakan paradigma Berorientasi Objek (Object-Oriented Programming / OOP) dalam bahasa Python. Aplikasi ini memfasilitasi pengelolaan jenis layanan laundry, data pelanggan beserta deposit saldo, pencatatan transaksi, perhitungan diskon otomatis, serta cetak nota transaksi.

---

1. Arsitektur & Struktur Class

  Program ini dibangun oleh "3 Class Utama" yang saling berinteraksi:

  A. `LayananLaundry`
  Mengelola informasi katalog layanan laundry dan kalkulasi estimasi waktu pengerjaan.
  - Atribut Kelas: `nama_instansi` (Nama identitas bisnis laundry).
  - Atribut Encapsulated (Private): `__tarif_per_kg` (Menggunakan `@property` & `@setter` dengan validasi nilai > 0).
  - Method:
    - `info_layanan()` (Instance Method): Mengembalikan string perincian layanan.
    - `dari_dict(cls, data)` (Class Method): Factory method untuk menginstansiasi objek dari tipe dictionary.
    - `hitung_estimasi_selesai(estimasi_hari)` (Static Method): Menghitung waktu penyelesaian laundry berbasis `datetime`.

  B. `Pelanggan`
  Mengelola profil identitas pelanggan dan saldo deposit pembayaran.
  - Atribut Kelas: `diskon_member` (Rasio persentase diskon potongan harga global).
  - Atribut Encapsulated (Private): `__saldo` (Menggunakan `@property` & `@setter` dengan validasi nilai >= 0).
  - Method:
    - `tambah_saldo(nominal)` & `kurangi_saldo(nominal)` (Instance Method): Mengelola transaksi deposit saldo pelanggan.
    - `ubah_diskon_member(cls, persen_baru)` (Class Method): Mengubah besaran diskon member global.
    - `validasi_no_telp(no_telp)` (Static Method): Memeriksa keabsahan format nomor telepon pelanggan.

  C. `Transaksi`
  Menjadi 'orchestrator' yang menghubungkan objek `Pelanggan` dan `LayananLaundry` untuk memproses pesanan dan pembayaran.
  - Atribut Kelas: `total_transaksi` (Penghitung otomatis jumlah transaksi yang diinstansiasi).
  - Atribut Encapsulated (Private): `__berat_kg`, `__status_pembayaran`, `__total_harga`.
  - Method:
    - `proses_pembayaran_saldo()` & `bayar_tunai(jumlah_uang)` (Instance Method): Memproses pelunasan transaksi.
    - `cetak_nota()` (Instance Method): Menampilkan nota transaksi ke konsol.
    - `reset_counter_transaksi(cls)` (Class Method): Mereset penghitung jumlah transaksi kelas.
    - `format_rupiah(nominal)` (Static Method): Menerapkan formatting standar mata uang Rupiah.

2. Panduan Menjalankan Program

  1. Pastikan Python versi 3.x telah terinstal di sistem.
  2. Unduh atau 'clone' repositori ini ke komputer.
  3. Buka terminal, lalu arahkan ke direktori proyek.
  4. Jalankan perintah "python main.py" berikut untuk mengeksekusi program beserta skenario pengujiannya 

3. Panduan Pengujian Program
  A. Pengujian Instansiasi Objek & Class Method
    Membuat minimal 2 objek untuk setiap class (layanan1 & layanan2, pelanggan1 & pelanggan2, trans1 & trans2).
    Pengujian pembentukan objek layanan menggunakan factory method LayananLaundry.dari_dict().
    Mengubah atribut kelas diskon member global via Pelanggan.ubah_diskon_member(0.15) dan melacak penghitung transaksi via Transaksi.total_transaksi.
  B. Pengujian Eksekusi Method
    Panggilan static method Pelanggan.validasi_no_telp() untuk memeriksa nomor telepon valid (081234567890) dan invalid (123-abc).
    Panggilan static method LayananLaundry.hitung_estimasi_selesai() untuk estimasi tanggal selesai.
    Panggilan instance method info_layanan(), proses_pembayaran_saldo(), tambah_saldo(), bayar_tunai(), serta cetak_nota().
  C. Pengujian Setter
    LayananLaundry.tarif_per_kg:
      Data Valid (8500): Berhasil memperbarui tarif layanan.
      Data Invalid (-5000): Memicu ValueError ("Tarif per kg harus berupa angka positif lebih dari 0!").
    Pelanggan.saldo:
      Data Valid (100000): Berhasil memperbarui saldo deposit.
      Data Invalid (-20000): Memicu ValueError ("Saldo deposit tidak boleh bernilai negatif!").
    Transaksi.berat_kg:
      Data Valid (5.5): Berhasil memperbarui berat cucian dan mengakulasi ulang total harga.
      Data Invalid (0): Memicu ValueError ("Berat cucian harus berupa angka positif dan lebih dari 0 kg!").