from datetime import datetime, timedelta


class LayananLaundry:
    nama_instansi = "CleanWash Express"

    def __init__(self, id_layanan: str, nama_layanan: str, tarif_per_kg: float, estimasi_hari: int):
        self.id_layanan = id_layanan
        self.nama_layanan = nama_layanan
        self.estimasi_hari = estimasi_hari
        
        self.__tarif_per_kg = 0.0
        self.tarif_per_kg = tarif_per_kg

    @property
    def tarif_per_kg(self) -> float:
        return self.__tarif_per_kg

    @tarif_per_kg.setter
    def tarif_per_kg(self, nilai: float):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            raise ValueError("Tarif per kg harus berupa angka positif lebih dari 0!")
        self.__tarif_per_kg = float(nilai)

    def info_layanan(self) -> str:
        return f"[{self.id_layanan}] {self.nama_layanan} | Rp {self.__tarif_per_kg:,.0f}/kg | Estimasi {self.estimasi_hari} Hari"

    @classmethod
    def dari_dict(cls, data: dict):
        """Membuat objek LayananLaundry dari struktur data dictionary."""
        return cls(
            id_layanan=data["id"],
            nama_layanan=data["nama"],
            tarif_per_kg=data["tarif"],
            estimasi_hari=data["estimasi"]
        )

    @staticmethod
    def hitung_estimasi_selesai(estimasi_hari: int, tanggal_mulai: datetime = None) -> str:
        """Menghitung tanggal dan waktu penyelesaian pesanan."""
        if tanggal_mulai is None:
            tanggal_mulai = datetime.now()
        tanggal_selesai = tanggal_mulai + timedelta(days=estimasi_hari)
        return tanggal_selesai.strftime("%d-%m-%Y %H:%M WIB")


class Pelanggan:
    diskon_member = 0.10

    def __init__(self, id_pelanggan: str, nama: str, no_telp: str, saldo: float = 0.0):
        if not nama or not nama.strip():
            raise ValueError("Nama pelanggan tidak boleh kosong atau hanya berisi spasi!")

        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.no_telp = no_telp
        
        self.__saldo = 0.0
        self.saldo = saldo

    @property
    def saldo(self) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai: float):
        if not isinstance(nilai, (int, float)) or nilai < 0:
            raise ValueError("Saldo deposit tidak boleh bernilai negatif!")
        self.__saldo = float(nilai)

    def tambah_saldo(self, nominal: float):
        if not isinstance(nominal, (int, float)) or nominal <= 0:
            raise ValueError("Nominal penambahan saldo harus angka positif lebih dari 0!")
        self.__saldo += nominal
        print(f"[DEPOSIT] Berhasil menambah Rp {nominal:,.0f} ke akun {self.nama}. Saldo sekarang: Rp {self.__saldo:,.0f}")

    def kurangi_saldo(self, nominal: float):
        if nominal > self.__saldo:
            raise ValueError(f"Saldo {self.nama} tidak mencukupi! Tersedia: Rp {self.__saldo:,.0f}, Dibutuhkan: Rp {nominal:,.0f}")
        self.__saldo -= nominal

    @classmethod
    def ubah_diskon_member(cls, persen_baru: float):
        """Mengubah persentase diskon kelas pelanggan secara global."""
        if not isinstance(persen_baru, (int, float)) or not (0.0 <= persen_baru <= 1.0):
            raise ValueError("Diskon member harus berupa rasio 0.0 sampai 1.0 (contoh: 0.15 untuk 15%)!")
        cls.diskon_member = persen_baru
        print(f"[SISTEM] Diskon member global diperbarui menjadi {cls.diskon_member * 100:.0f}%")

    @staticmethod
    def validasi_no_telp(no_telp: str) -> bool:
        """Memeriksa apakah format nomor telepon berupa digit dengan panjang logis."""
        cleaned = no_telp.replace("-", "").replace(" ", "").replace("+", "")
        return cleaned.isdigit() and (10 <= len(cleaned) <= 14)


class Transaksi:
    total_transaksi = 0

    def __init__(self, id_transaksi: str, pelanggan: Pelanggan, layanan: LayananLaundry, berat_kg: float):
        self.id_transaksi = id_transaksi
        self.pelanggan = pelanggan
        self.layanan = layanan
        
        self.__berat_kg = 0.0
        self.__status_pembayaran = "Belum Lunas"
        self.__total_harga = 0.0
        
        self.berat_kg = berat_kg
        
        Transaksi.total_transaksi += 1

    @property
    def berat_kg(self) -> float:
        return self.__berat_kg

    @berat_kg.setter
    def berat_kg(self, nilai: float):
        if not isinstance(nilai, (int, float)) or nilai <= 0:
            raise ValueError("Berat cucian harus berupa angka positif dan lebih dari 0 kg!")
        self.__berat_kg = float(nilai)
        self.__total_harga = self._hitung_total()

    @property
    def status_pembayaran(self) -> str:
        return self.__status_pembayaran

    @property
    def total_harga(self) -> float:
        return self.__total_harga

    def _hitung_total(self) -> float:
        subtotal = self.layanan.tarif_per_kg * self.__berat_kg
        potongan = subtotal * Pelanggan.diskon_member
        return subtotal - potongan

    def proses_pembayaran_saldo(self) -> bool:
        if self.__status_pembayaran.startswith("Lunas"):
            print(f"[BAYAR] Transaksi {self.id_transaksi} sudah lunas sebelumnya.")
            return True

        if self.pelanggan.saldo >= self.__total_harga:
            self.pelanggan.kurangi_saldo(self.__total_harga)
            self.__status_pembayaran = "Lunas (Deposit Saldo)"
            print(f"[BAYAR SUCCESS] Transaksi {self.id_transaksi} lunas menggunakan saldo {self.pelanggan.nama}.")
            return True
        else:
            kekurangan = self.__total_harga - self.pelanggan.saldo
            print(f"[BAYAR GAGAL] Saldo {self.pelanggan.nama} kurang Rp {kekurangan:,.0f}!")
            return False

    def bayar_tunai(self, jumlah_uang: float):
        if jumlah_uang < self.__total_harga:
            raise ValueError(f"Uang tunai tidak mencukupi! Total: Rp {self.__total_harga:,.0f}, Diterima: Rp {jumlah_uang:,.0f}")
        kembalian = jumlah_uang - self.__total_harga
        self.__status_pembayaran = "Lunas (Tunai)"
        print(f"[BAYAR SUCCESS] Transaksi {self.id_transaksi} lunas via Tunai. Kembalian: Rp {kembalian:,.0f}")

    def cetak_nota(self):
        est = LayananLaundry.hitung_estimasi_selesai(self.layanan.estimasi_hari)
        print("=" * 50)
        print(f"          NOTA TRANSAKSI {LayananLaundry.nama_instansi.upper()}")
        print("=" * 50)
        print(f"ID Transaksi : {self.id_transaksi}")
        print(f"Pelanggan    : {self.pelanggan.nama} [{self.pelanggan.id_pelanggan}]")
        print(f"Layanan      : {self.layanan.nama_layanan}")
        print(f"Berat Cucian : {self.berat_kg} kg")
        print(f"Tarif per kg : Rp {self.layanan.tarif_per_kg:,.0f}")
        print(f"Diskon Member: {Pelanggan.diskon_member * 100:.0f}%")
        print(f"Total Bayar  : Rp {self.__total_harga:,.0f}")
        print(f"Status Bayar : {self.__status_pembayaran}")
        print(f"Est. Selesai : {est}")
        print("=" * 50 + "\n")

    @classmethod
    def reset_counter_transaksi(cls):
        """Mereset akumulator atribut kelas total_transaksi."""
        cls.total_transaksi = 0
        print("[SISTEM] Counter total transaksi berhasil di-reset ke 0.")

    @staticmethod
    def format_rupiah(nominal: float) -> str:
        return f"Rp {nominal:,.2f}"

if __name__ == "__main__":
    print("\n" + "="*60)
    print(" DEMONSTRASI SISTEM LAUNDRY 'CLEANWASH' ")
    print("="*60 + "\n")

    print("--- 1. Inisialisasi Objek ---")
    
    layanan1 = LayananLaundry("LYN01", "Reguler Cuci Setrika", 7000, 2)
    dict_layanan = {"id": "LYN02", "nama": "Express Kilat", "tarif": 12000, "estimasi": 1}
    layanan2 = LayananLaundry.dari_dict(dict_layanan)

    pelanggan1 = Pelanggan("CUST01", "Budi Santoso", "081234567890", saldo=50000)
    pelanggan2 = Pelanggan("CUST02", "Siti Rahma", "089876543210", saldo=15000)

    trans1 = Transaksi("TRX001", pelanggan1, layanan1, berat_kg=4.0)
    trans2 = Transaksi("TRX002", pelanggan2, layanan2, berat_kg=2.5)

    print(f"Berhasil membuat objek layanan, pelanggan, dan transaksi.")
    print(f"Atribut Kelas total_transaksi saat ini: {Transaksi.total_transaksi}\n")

    print("--- 2. Demonstrasi Eksekusi Method ---")
    
    telp_valid = Pelanggan.validasi_no_telp(pelanggan1.no_telp)
    telp_invalid = Pelanggan.validasi_no_telp("123-abc")
    print(f"[Static Method] Validasi Telp '{pelanggan1.no_telp}': {telp_valid}")
    print(f"[Static Method] Validasi Telp '123-abc': {telp_invalid}")
    print(f"[Static Method] Format Rupiah: {Transaksi.format_rupiah(125000)}")
    
    est_selesai = LayananLaundry.hitung_estimasi_selesai(layanan1.estimasi_hari)
    print(f"[Static Method] Estimasi LYN01 Selesai: {est_selesai}\n")

    print("[Instance Method] Menampilkan Info Layanan:")
    print(" ", layanan1.info_layanan())
    print(" ", layanan2.info_layanan())
    print()

    print("[Instance Method] Memproses Pembayaran Transaksi 1 (Siti/Saldo kurang):")
    trans2.proses_pembayaran_saldo()

    print("\n[Instance Method] Menambah Saldo Pelanggan 2:")
    pelanggan2.tambah_saldo(30000)

    print("\n[Instance Method] Memproses Ulang Pembayaran Transaksi 1:")
    trans2.proses_pembayaran_saldo()
    print()

    print("[Class Method] Mengubah diskon member global:")
    Pelanggan.ubah_diskon_member(0.15)
    
    trans1.berat_kg = 4.0
    trans1.bayar_tunai(30000)
    print()

    trans1.cetak_nota()
    trans2.cetak_nota()

    print("--- 3. Pengujian Validasi Setter Encapsulation (Try-Except) ---")

    print("\n[UJI SETTER] Modifikasi Tarif Layanan 1")
    try:
        layanan1.tarif_per_kg = 8500
        print(f"-> VALID: Tarif berhasil diubah ke Rp {layanan1.tarif_per_kg:,.0f}")
    except ValueError as e:
        print(f"-> GAGAL: {e}")

    try:
        layanan1.tarif_per_kg = -5000
        print(f"-> VALID: Tarif berhasil diubah ke {layanan1.tarif_per_kg}")
    except ValueError as e:
        print(f"-> TERDAPAT ERROR (Sesuai Ekspektasi): {e}")

    print("\n[UJI SETTER] Modifikasi Saldo Pelanggan 1")
    try:
        pelanggan1.saldo = 100000
        print(f"-> VALID: Saldo berhasil diubah ke Rp {pelanggan1.saldo:,.0f}")
    except ValueError as e:
        print(f"-> GAGAL: {e}")

    try:
        pelanggan1.saldo = -20000
        print(f"-> VALID: Saldo berhasil diubah ke {pelanggan1.saldo}")
    except ValueError as e:
        print(f"-> TERDAPAT ERROR (Sesuai Ekspektasi): {e}")

    print("\n[UJI SETTER] Modifikasi Berat Cucian Transaksi 1")
    try:
        trans1.berat_kg = 5.5
        print(f"-> VALID: Berat berhasil diubah ke {trans1.berat_kg} kg")
    except ValueError as e:
        print(f"-> GAGAL: {e}")

    try:
        trans1.berat_kg = 0
        print(f"-> VALID: Berat berhasil diubah ke {trans1.berat_kg} kg")
    except ValueError as e:
        print(f"-> TERDAPAT ERROR (Sesuai Ekspektasi): {e}")

    print("\n" + "="*60)
    print(" SELURUH PENGUJIAN SELESAI DAN VALID ")
    print("="*60 + "\n")