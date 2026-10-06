from datetime import datetime, timedelta

class LayananLaundry:
    nama_instansi = "CleanWash Express"

    def __init__(self, id_layanan, nama_layanan, tarif_per_kg, estimasi_hari):
        self.id_layanan = id_layanan
        self.nama_layanan = nama_layanan
        self.estimasi_hari = estimasi_hari
        
        self._tarif_per_kg = 0.0
        self.tarif_per_kg = tarif_per_kg

    @property
    def tarif_per_kg(self):
        return self._tarif_per_kg

    @tarif_per_kg.setter
    def tarif_per_kg(self, nilai):
        if nilai <= 0:
            raise ValueError("Tarif per kg harus berupa angka positif lebih dari 0!")
        self._tarif_per_kg = float(nilai)

    def info_layanan(self):
        return f"[{self.id_layanan}] {self.nama_layanan} | Rp {self._tarif_per_kg:,.0f}/kg | Est {self.estimasi_hari} Hari"

    @classmethod
    def dari_dict(cls, data):
        return cls(
            id_layanan=data["id"],
            nama_layanan=data["nama"],
            tarif_per_kg=data["tarif"],
            estimasi_hari=data["estimasi"]
        )

    @staticmethod
    def hitung_estimasi_selesai(estimasi_hari, tanggal_mulai=None):
        if tanggal_mulai is None:
            tanggal_mulai = datetime.now()
        tanggal_selesai = tanggal_mulai + timedelta(days=estimasi_hari)
        return tanggal_selesai.strftime("%d-%m-%Y %H:%M WIB")

class LayananReguler(LayananLaundry):
    def __init__(self, id_layanan, nama_layanan, tarif_per_kg, estimasi_hari, jenis_pewangi):
        super().__init__(id_layanan, nama_layanan, tarif_per_kg, estimasi_hari)
        self.jenis_pewangi = jenis_pewangi

    def info_layanan(self):
        return f"[{self.id_layanan}] {self.nama_layanan} (Reguler) | Pewangi: {self.jenis_pewangi} | Rp {self._tarif_per_kg:,.0f}/kg"

class LayananExpress(LayananLaundry):
    def __init__(self, id_layanan, nama_layanan, tarif_per_kg, estimasi_hari, biaya_tambahan):
        super().__init__(id_layanan, nama_layanan, tarif_per_kg, estimasi_hari)
        self.biaya_tambahan = biaya_tambahan

    def info_layanan(self):
        total_tarif = self._tarif_per_kg + self.biaya_tambahan
        return f"[{self.id_layanan}] {self.nama_layanan} (Express) | Ekstra: Rp {self.biaya_tambahan:,.0f} | Total: Rp {total_tarif:,.0f}/kg"

class Pelanggan:
    diskon_member = 0.10

    def __init__(self, id_pelanggan, nama, no_telp, saldo=0.0):
        if not nama or not nama.strip():
            raise ValueError("Nama pelanggan tidak boleh kosong atau hanya berisi spasi!")

        self.id_pelanggan = id_pelanggan
        self.nama = nama
        self.no_telp = no_telp
        
        self.__saldo = 0.0
        self.saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            raise ValueError("Saldo deposit tidak boleh bernilai negatif!")
        self.__saldo = float(nilai)

    def tambah_saldo(self, nominal):
        if nominal <= 0:
            raise ValueError("Nominal harus lebih dari 0!")
        self.__saldo += nominal

    def kurangi_saldo(self, nominal):
        if nominal > self.__saldo:
            raise ValueError(f"Saldo tidak mencukupi! Tersedia: Rp {self.__saldo:,.0f}")
        self.__saldo -= nominal

    @classmethod
    def ubah_diskon_member(cls, persen_baru):
        if persen_baru < 0.0 or persen_baru > 1.0:
            raise ValueError("Diskon member harus berupa rasio 0.0 sampai 1.0 (contoh: 0.15 untuk 15%)!")
        cls.diskon_member = persen_baru
        print(f"Diskon member global diperbarui menjadi {cls.diskon_member * 100:.0f}%")

    @staticmethod
    def validasi_no_telp(no_telp):
        cleaned = no_telp.replace("-", "").replace(" ", "").replace("+", "")
        return cleaned.isdigit() and (10 <= len(cleaned) <= 14)

class Karyawan:
    def __init__(self, id_karyawan, nama, posisi):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.posisi = posisi

    def layani_pelanggan(self, pelanggan):
        print(f"-> Karyawan {self.nama} ({self.posisi}) sedang melayani pelanggan: {pelanggan.nama}")

class CabangLaundry:
    def __init__(self, nama_cabang, lokasi):
        self.nama_cabang = nama_cabang
        self.lokasi = lokasi
        self._karyawan = []

    def tambah_karyawan(self, karyawan):
        self._karyawan.append(karyawan)
        print(f"-> Karyawan '{karyawan.nama}' berhasil ditempatkan di cabang {self.nama_cabang}")

    def tampilkan_info(self):
        print(f"--- Info Cabang {self.nama_cabang} ---")
        for k in self._karyawan:
            print(f"  - {k.nama} ({k.posisi})")

class ItemCucian:
    def __init__(self, nama_pakaian, jumlah, berat):
        self.nama_pakaian = nama_pakaian
        self.jumlah = jumlah
        self.berat = berat

class Transaksi:
    total_transaksi = 0

    def __init__(self, id_transaksi, pelanggan, layanan):
        self.id_transaksi = id_transaksi
        self.pelanggan = pelanggan
        self.layanan = layanan
        
        self._item_cucian = [] 
        
        self.__berat_kg = 0.0
        self.__status_pembayaran = "Belum Lunas"
        self.__total_harga = 0.0
        
        Transaksi.total_transaksi += 1

    def tambah_item(self, nama_pakaian, jumlah, berat):
        if berat <= 0 or jumlah <= 0:
            raise ValueError("Jumlah dan berat harus > 0!")
            
        item_baru = ItemCucian(nama_pakaian, jumlah, berat)
        self._item_cucian.append(item_baru)
        
        self.__berat_kg += berat
        self.__total_harga = self._hitung_total()
        print(f"-> [+] Item '{nama_pakaian}' ({jumlah} pcs, {berat} kg) ditambahkan ke {self.id_transaksi}")

    @property
    def berat_kg(self):
        return self.__berat_kg
    
    @berat_kg.setter
    def berat_kg(self, nilai):
        if nilai <= 0:
            raise ValueError("Berat cucian harus berupa angka positif dan lebih dari 0 kg!")
        self.__berat_kg = float(nilai)
        self.__total_harga = self._hitung_total()

    @property
    def status_pembayaran(self):
        return self.__status_pembayaran
    
    @property
    def total_harga(self):
        return self.__total_harga

    def _hitung_total(self):
        tarif_aktif = self.layanan.tarif_per_kg
        if hasattr(self.layanan, 'biaya_tambahan'):
            tarif_aktif += self.layanan.biaya_tambahan
            
        subtotal = tarif_aktif * self.__berat_kg
        potongan = subtotal * Pelanggan.diskon_member
        return subtotal - potongan

    def proses_pembayaran_saldo(self):
        if self.__status_pembayaran.startswith("Lunas"):
            print(f"Transaksi {self.id_transaksi} sudah lunas sebelumnya.")
            return True
        
        if self.pelanggan.saldo >= self.__total_harga:
            self.pelanggan.kurangi_saldo(self.__total_harga)
            self.__status_pembayaran = "Lunas (Deposit Saldo)"
            return True
        else:
            kekurangan = self.__total_harga - self.pelanggan.saldo
            print(f"Saldo {self.pelanggan.nama} kurang Rp {kekurangan:,.0f}!")
            return False
    
    def bayar_tunai(self, jumlah_uang):
        if jumlah_uang < self.__total_harga:
            raise ValueError(f"Uang tunai tidak mencukupi! Total: Rp {self.__total_harga:,.0f}, Diterima: Rp {jumlah_uang:,.0f}")
        kembalian = jumlah_uang - self.__total_harga
        self.__status_pembayaran = "Lunas (Tunai)"
        print(f"Transaksi {self.id_transaksi} lunas via Tunai. Kembalian: Rp {kembalian:,.0f}")

    def cetak_nota(self):
        est = LayananLaundry.hitung_estimasi_selesai(self.layanan.estimasi_hari)
        print("\n" + "=" * 45)
        print(f"      NOTA TRANSAKSI - {self.id_transaksi}")
        print("=" * 45)
        print(f"Pelanggan    : {self.pelanggan.nama}")
        print(f"Layanan      : {self.layanan.info_layanan()}")
        print("Daftar Cucian:")
        for i, item in enumerate(self._item_cucian, 1):
            print(f"  {i}. {item.nama_pakaian} ({item.jumlah} pcs) - {item.berat} kg")
        print(f"Total Berat  : {self.__berat_kg} kg")
        print(f"Diskon Member: {Pelanggan.diskon_member * 100:.0f}%")
        print(f"Total Bayar  : Rp {self.__total_harga:,.0f}")
        print(f"Status       : {self.__status_pembayaran}")
        print(f"Est. Selesai : {est}")
        print("=" * 45 + "/n")

        @classmethod
        def reset_counter_transaksi(cls):
            cls.total_transaksi = 0
            print("Counter total transaksi berhasil di-reset ke 0.")

        @staticmethod
        def format_rupiah(nominal):
            return f"Rp {nominal:,.2f}"


print("\nUJI AGREGASI & ASOSIASI")
cabang_unmul = CabangLaundry("CleanWash Unmul", "Gedung Fakultas")
karyawan1 = Karyawan("EMP01", "Fajar", "Front Desk")
karyawan2 = Karyawan("EMP02", "Dina", "Operator Cuci")

cabang_unmul.tambah_karyawan(karyawan1)
cabang_unmul.tambah_karyawan(karyawan2)
cabang_unmul.tampilkan_info()

pelanggan1 = Pelanggan("CUST01", "Ahmad", "081234567", 100000)
karyawan1.layani_pelanggan(pelanggan1)

print("\nUJI INHERITANCE")
layanan_reg = LayananReguler("LYN-R", "Reguler Cuci Kering", 7000, 3, "Lavender")
layanan_exp = LayananExpress("LYN-E", "Super Kilat", 7000, 1, 5000)

print(layanan_reg.info_layanan())
print(layanan_exp.info_layanan())

print("\nUJI KOMPOSISI")
transaksi_reguler = Transaksi("TRANSAKSI-001", pelanggan1, layanan_reg)
transaksi_reguler.tambah_item("Kemeja Flanel", 3, 1.5)
transaksi_reguler.tambah_item("Celana Jeans", 2, 2.0)

transaksi_express = Transaksi("TRANSAKSI-002", pelanggan1, layanan_exp)
transaksi_express.tambah_item("Jas Almamater", 1, 1.2)

transaksi_reguler.proses_pembayaran_saldo()
transaksi_reguler.cetak_nota()
transaksi_express.cetak_nota()