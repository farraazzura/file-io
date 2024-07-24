# buka file
file_pantun = open("pantun.txt", "r")

# baca isi semua file
# pantun = file_pantun.read()

# baca isi berdasarkan baris file semua baris
pantun = file_pantun.readlines()

# cetak isi file dengan perulangan
# for teks in puisi:
#   print(teks) rhhrthrthryry

# baca isi berdasarkan baris file satu baris teratas
# pantun = file_pantun.readline()

# cetak semua baris
# print(pantun)

# cetak baris pertama
print(pantun[0] )

# cetak baris kedua
print(pantun[1] )

# tutup file
file_pantun.close( )
