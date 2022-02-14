#Menghitung berat badan yang diperlukan dalam Body Mass Index

#Informasi program
print("++++Selamat datang di program pencari berat badan!+++++")
print(" ")
print("+++Informasi Nilai BMI+++")
print("Underweight = <18.5 \nNormal weight = 18.5-24.9 \nOverweight = 25-29.9 \nObesity = BMI of 30 or greater")
print(" ")
#inisiasi Variabel an input
bmi = float(input("Masukan Nilai BMI anda = "))
tinggi = float(input("Masukan tinggi badan anda dalam meter = "))
#Mengubah tinggi dari meter menjadi centimeter
tinggicm= tinggi *100
#rumus
berat = (tinggicm**2)*bmi/10000

#output
print("Berat badan yang diperlukan dalam Kilogram =", int(berat))