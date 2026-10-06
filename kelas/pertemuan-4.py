# class Nasabah:
#     def __init__(self, nama, nomor_rekening, saldo):
#         self.nama = nama
#         self.nomor_rekening = nomor_rekening
#         self.saldo = saldo

#     def tarik_tunai(self, atm, jumlah):
#         self.saldo -= jumlah
#         atm.saldo_kas -= jumlah

# class MesinATM:
#     def __init__(self, id_atm, lokasi, saldo_kas):
#         self.id_atm = id_atm
#         self.lokasi = lokasi
#         self.saldo_kas = saldo_kas

#     def proses_penarikan(self, nama_nasabah, jumlah):
#         if jumlah <= self.saldo_kas:
#             self.saldo_kas -= jumlah
#             print(f" [ATM {self.id_atm}] Penarikan Rp{jumlah:,} oleh {nama_nasabah} berhasil.")
#             print(f" Sisa kas di ATM {self.lokasi}: Rp{self.saldo_kas:,}")
#         else:
#             print(f" [ATM {self.id_atm}] Saldo kas mesin tidak mencukupi.")


# # Kedua objek dibuat secara independen
# atm_pusat = MesinATM("ATM-01", "Kantor Cabang Sudirman", 50000000)
# budi = Nasabah("Budi Santoso", "101-220-334", 500)
# siti = Nasabah("Siti Rahma", "101-445-889", 1000)
# # Asosiasi berjalan saat method dipanggil
# budi.tarik_tunai(atm_pusat, 500000)
# # Mesin ATM yang sama bisa digunakan oleh nasabah lain
# siti.tarik_tunai(atm_pusat, 1000000)

# print(siti.saldo)

# class Bank:
#     def __init__(self, nama_bank, kode):
#         self.nama_bank = nama_bank
#         self.kode = kode
#         self.karyawan = []

#     def tambah_karyawan(self, nama, nip, posisi):
#         karyawan_baru = Karyawan(nama, nip, posisi)
#         self.karyawan.append(karyawan_baru)


# class Karyawan:
#     def __init__(self, nama, nip, posisi):
#         self.nama = nama
#         self.nip = nip
#         self.posisi = posisi

# bank = Bank("BCA", "12346", 10)
# bank.tambah_karyawan("udin", "013", "Pegawai")  
# bank.tambah_karyawan("dapa", "012", "Manager")

# print(bank.karyawan[1])
# print(bank.karyawan[1].nama)

class Order:
    def __init__(self, id_order, nama_pelanggan, total_harga):
        self.id_order = id_order
        self.nama_pelanggan = nama_pelanggan
        self.total_harga = total_harga
        self.item = []

    def tambah_item(self, nama_item, harga):
        item_baru = Item(nama_item, harga)
        self.item.append(item_baru)