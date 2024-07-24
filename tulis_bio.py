print("Selamat Datang di Program Biodata Farra")
print("=================================")

# ambil input dari user 
nama = input("Nama: ")
umur = input("Umur: ")
alamat = input("Alamat: ")

# format teks 
teks = "\nNama: " + nama + "\nUmur: " + umur + "\nAlamat: " + alamat + "\n---"#jika ingin format mendatar, cukup hapus /n 

# buka file 
buka_file = open("biodata.txt", "a")

# menulis data ke dalam file 
tulis_file = buka_file.write(teks)

# print kalimat validasi bahwa data berhasil ditulis kedalam file 
print("Data berhasil ditambahkan")

# tutup file 
buka_file.close()