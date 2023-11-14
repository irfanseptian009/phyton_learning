# Import library PyKnow
from pyknow import *

# Definisikan fakta-fakta sebagai kelas
class Fakta(Fact):
    pass

# Definisikan aturan-aturan sebagai kelas
class Aturan(KnowledgeEngine):
    # R1: Jika pembeli memiliki uang memiliki uang Rp 7Jt dan dia ingin memilih laptop yang VGAnya bagus maka dia membeli merek Toshiba
    @Rule(Fakta(uang='Rp 7Jt'), Fakta(vga='bagus'))
    def r1(self):
        print("Rekomendasi: Merek Toshiba")

    # R2: Jika pembeli ingin memilih laptop yang prosesornya cepat dan dia ingin memilih laptop yang VGAnya bagus maka dia membeli merek Asus
    @Rule(Fakta(prosesor='cepat'), Fakta(vga='bagus'))
    def r2(self):
        print("Rekomendasi: Merek Asus")

    # R3: Jika pembeli memiliki uang Rp 10Jt dan dia ingin memilih laptop yang prosesornya cepat maka dia membeli merek Asus
    @Rule(Fakta(uang='Rp 10Jt'), Fakta(prosesor='cepat'))
    def r3(self):
        print("Rekomendasi: Merek Asus")

    # R4: Jika pembeli memiliki uang Rp 10Jt maka dia ingin memilih laptop yang kamerannya bagus
    @Rule(Fakta(uang='Rp 10Jt'))
    def r4(self):
        print("Rekomendasi: Laptop yang kamerannya bagus")

    # R5: Jika pembeli ingin memilih laptop yang prosesornya cepat maka dia membeli merek IBM
    @Rule(Fakta(prosesor='cepat'))
    def r5(self):
        print("Rekomendasi: Merek IBM")

# Buat objek dari kelas Aturan
aturan = Aturan()

# Reset dan jalankan sistem pakar
aturan.reset()
aturan.run()

# Masukkan fakta-fakta yang diketahui
aturan.declare(Fakta(uang='Rp 7Jt'))
aturan.declare(Fakta(prosesor='cepat'))
aturan.declare(Fakta(vga='bagus'))

# Lihat output rekomendasi laptop
# Output: Rekomendasi: Merek Toshiba
#         Rekomendasi: Merek Asus
#         Rekomendasi: Merek IBM
