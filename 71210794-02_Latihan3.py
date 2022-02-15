#latihan soal no 3 minggu 2

#variabel dan input
gaji_perjam = int(input("Masukan Gaji per-jam yang anda inginkan = "))
kerja_jam = int(input("Masukan Berapa jam yang akan anda kerjakan dalam satu minggu = "))

#output
reversepajak= 86/100
gaji_tidak_pajak = gaji_perjam * kerja_jam
gaji_pajak= gaji_tidak_pajak * reversepajak
pakaian_aksesoris = gaji_pajak * 10/100
gaji_kurang1 = gaji_pajak - pakaian_aksesoris
alat_tulis= gaji_kurang1 * 1/100
gaji_kurang2 = gaji_kurang1 - alat_tulis
sedekah= gaji_kurang2 * 25/100

anak_yatim = sedekah * 30/100
anak_dhuafa = sedekah * 70/100




print("Gaji bersih Budi =", gaji_tidak_pajak)
print("Gaji Budi dengan pajak 14% =", int(gaji_pajak) )
print("Jumlah uang Budi untuk membeli pakaian dan aksesoris = ",int(pakaian_aksesoris))
print("Jumlah uang Budi untuk membeli alat tulis =", int(alat_tulis))
print("Jumlah uang Budi untuk sedekah =", int(sedekah))
print("Jumlah uang sedekah untuk anak yatim =", int(anak_yatim))
print("Jumlah uang sedekah untuk anak dhuafa =", int(anak_dhuafa))