# class Animal:

#     def __init__(self, nama, umur):
#         self.nama = nama
#         self.umur = umur

# class Mamalia(Animal):

#     def __init__(self, nama, umur, warna_bulu):
#         super().__init__(nama, umur)
#         self.warna_bulu = warna_bulu

# class Reptil(Animal):

#     def __init__(self, nama, umur, berbisa):
#         super().__init__(nama, umur)
#         self.berbisa = berbisa

# kucing = Mamalia("oren", 1, "oren")
# ular_cobra = Reptil("cobra", 2, True)

# print(kucing.nama)
# print(ular_cobra.nama)
# print(kucing.warna_bulu)
# print(ular_cobra.berbisa)

class Teller(Karyawan):
    def __init__(self, nama, nip):
        super().__init__(nama, nip, "Teller")

    def layani_setoran(self, rekening, nominal):
        # Asosiasi: rekening diterima sebagai parameter method
        print(f" Teller {self.nama} melayani setoran...")
        rekening.setor(nominal, f"Setoran via teller {self.nip}")

class ManajerCabang(Karyawan):
    def __init__(self, nama, nip):
        super().__init__(nama, nip, "Branch Manager")

    def setujui_overdraft(self, rekening_giro, batas_baru):
        rekening_giro.batas_overdraft = batas_baru
        print(f" {self.nama} menyetujui batas overdraft Rp{batas_baru:,}untuk {rekening_giro.nama_pemilik}")

class MesinATM:
    def __init__(self, id_atm, lokasi, saldo_kas):
        self.id_atm = id_atm
        self.lokasi = lokasi
        self.saldo_kas = saldo_kas

    def proses_penarikan(self, rekening, jumlah):
        if jumlah > self.saldo_kas:
            print(f" [ATM {self.id_atm}] Saldo kas mesin tidak mencukupi.")
            return
        saldo_sebelum = rekening.saldo
        rekening.tarik(jumlah, f"Tarik tunai ATM {self.id_atm}")
        if rekening.saldo < saldo_sebelum:
            self.saldo_kas -= jumlah

class Nasabah:
    def __init__(self, nama):
        self.nama = nama
        self._daftar_rekening = [] # Asosiasi: rekening dibuat diluar, lalu didaftarkan

    def tambah_rekening(self, rekening):
        self._daftar_rekening.append(rekening)

    def tarik_tunai(self, atm, rekening, jumlah):
        # Asosiasi: MesinATM dan Rekening diterima sebagai parameter
        print(f" {self.nama} memasukkan kartu ke ATM {atm.id_atm}")
        print(f" di {atm.lokasi}...")
        atm.proses_penarikan(rekening, jumlah)