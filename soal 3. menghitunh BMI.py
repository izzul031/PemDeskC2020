"""
Created on Oct 01 2020

@author: 190411100031/Nur Mu'izzul Qodir
"""

print("Program Menghitung Index Massa Tubuh / BMI")

berat = float(input("Masukan berat(kg): "))
tinggi = float(input("Masukan tinggi(m): "))

bmi = berat/(tinggi*tinggi)
print("Hasil Perhitungan: ", bmi)

if (bmi < 18.5):
    print("Berat badan kurang")
elif (bmi <= 22.9):
    print("Berat badan normal")
elif (bmi >= 29.9):
    print("Berat badan berlebih(kecenderungan obesitas)")
elif (bmi >= 30):
    print("Obesitas")
