import os

class Kicker():
    __jumlahKicker = 0

    def __init__(self, name, team, shotStat=0):
        self.name = name
        self.__team = team
        self.__shotStat = shotStat
        Kicker.__jumlahKicker += 1

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        if not isinstance(value, str):
            raise TypeError
        if value.lower() == "barca" or value.lower() == "madrid":
            self.__team = value.lower()
        else:
            raise ValueError

    @property
    def shotStat(self):
        return self.__shotStat

    @shotStat.setter
    def shotStat(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value >= 0:
            self.__shotStat = value
        else:
            raise ValueError

    @staticmethod
    def get_JumlahKicker():
        return Kicker.__jumlahKicker

class Keeper():
    __jumlahKeeper = 0
    
    def __init__(self, name, team, reachStat=0):
        self.name = name
        self.__team = team
        self.__reachStat = reachStat
        Keeper.__jumlahKeeper += 1

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        if not isinstance(value, str):
            raise TypeError    
        if value.lower() == "barca" or value.lower() == "madrid":
            self.__team = value.lower()
        else:
            raise ValueError

    @property
    def reachStat(self):
        return self.__reachStat

    @reachStat.setter
    def reachStat(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value >= 0:
            self.__reachStat = value
        else:
            raise ValueError

    @staticmethod
    def get_JumlahKeeper():
        return Keeper.__jumlahKeeper

class Match():
    __jumlahMatch = 0
    
    def __init__(self, skorA=0, skorB=0):
        self.__skorA = skorA
        self.__skorB = skorB
        self.__jumlahPutaran = skorA + skorB
        self.cekPutaranUp5()
        Match.__jumlahMatch += 1
        
    @property
    def jumlahPutaran(self):
        return self.__jumlahPutaran

    @jumlahPutaran.setter
    def jumlahPutaran(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value > 5:
            self.__jumlahPutaran = value % 5
        elif value < 0:
            raise ValueError
        else:
            self.__jumlahPutaran = value
        
    @classmethod
    def show_jumlahMatch(cls):
        print(f"Kedua tim sudah bertemu {cls.__jumlahMatch} kali pertandingan")

    def add_goal(self, team):
        if team ==  "barca":
            self.__skorA += 1
        elif team == "madrid":
            self.__skorB += 1
        else:
            raise ValueError
        self.__jumlahPutaran += 1
        self.cekPutaranUp5()
        
    def get_skor(self):
        return "Skor: {} - {}".format(self.__skorA,self.__skorB)

    def cekPutaranUp5(self):
        if self.jumlahPutaran > 5:
            self.jumlahPutaran %= 5

kicker1 = Kicker("Andi", "barca", 23)
kicker2 = Kicker("Budi", "madrid", 88)
keeper1 = Keeper("Anton", "madrid", 75)
keeper2 = Keeper("Beni", "barca", 80) 
match1 = Match(0, 0)
match2 = Match(3, 2)

os.system("cls")
print("=== CLI PENALTY SIMULATOR ===")
print("Jumlah penendang: ", Kicker.get_JumlahKicker())
print("Jumlah kiper: ", Keeper.get_JumlahKeeper())

print("Jumlah putaran match pertama: ", match1.jumlahPutaran)
match1.add_goal("barca")
print("Jumlah putaran match pertama (setelah memanngil fungsi add_goal): ", match1.jumlahPutaran)
print()

print("Jumlah putaran match kedua: ", match2.jumlahPutaran)
print(match2.get_skor())
match2.add_goal("barca")
print("Jumlah putaran match kedua (setelah memanggil fungsi add_goal dan mengecek apakah sudh 5 putaran lebih): ", match2.jumlahPutaran)
print(match2.get_skor())
Match.show_jumlahMatch()
print()

print(">> Pengujian setter dengan nilai valid")
print("Setter team pada objek kicker1:")
print("\t<-", kicker1.team)
kicker1.team = "madrid"
print("\t->", kicker1.team)

print("Setter shotStat pada objek kicker2:")
print("\t<-", kicker2.shotStat)
kicker2.shotStat = 23
print("\t->", kicker2.shotStat)

print("Setter team (saat input dengan kapital semua) pada objek keeper1:")
print("\t<-", keeper1.team)
keeper1.team = "BARCA"
print("\t->", keeper1.team)

print("Setter reachStat pada objek keeper2:")
print("\t<-", keeper2.reachStat)
keeper2.reachStat = 100
print("\t->", keeper2.reachStat)

print("Setter jumlahPutaran pada objek match1:")
print("\t<-", match1.jumlahPutaran)
match1.jumlahPutaran = 7
print("\t->", match1.jumlahPutaran)

print("\n>> Pengujian setter dengan nilai tidak valid")
print("Mengisi team kicker dengan 'chelsea':")
try:
    kicker1.team = "chelsea" 
except ValueError:
    print("\t-> Validasi berhasil: ValueError ditangkap. Tim hanya boleh 'barca' atau 'madrid'.")

print("Mengisi shotStat kicker dengan nilai negatif (-5):")
try:
    kicker2.shotStat = -5
except ValueError:
    print("\t-> Validasi berhasil: ValueError ditangkap. Nilai statistik tidak boleh negatif.")

print("Mengisi team keeper dengan string kosong (''):")
try:
    keeper1.team = ""
except ValueError:
    print("\t-> Validasi berhasil: ValueError ditangkap. Tim kosong tidak valid.")

print("Mengisi reachStat keeper dengan tipe data string ('ty'):")
try:
    keeper2.reachStat = "ty"
except TypeError:
    print("\t-> Validasi berhasil: TypeError ditangkap. Input harus berupa angka (integer).")

print("Mengisi jumlahPutaran match dengan string kosong (''):")
try:
    match1.jumlahPutaran = ""
except TypeError:
    print("\t-> Validasi berhasil: TypeError ditangkap. Input harus berupa angka (integer).")