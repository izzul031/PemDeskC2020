"""
Created on Oct 01 2020

@author: 190411100031/Nur Mu'izzul Qodir
"""

print("Program menentukan nilai maksimal dan minimal")

bil = []

banyak = int(input("Masukkan Nilai yang Ingin Diinputkan : "))
for i in range(banyak):
    nomor = int(input("Masukkan Angka: "))
    bil.append(nomor)

print("Bilangan yang Diinputkan", bil)
for i in range(len(bil)):
    for j in range(i+1, len(bil)):
        if bil[i] > bil[j]:
            bil[i],bil[j] = bil[j],bil[i]

print("Nilai Minimal", bil[0])
print("Nilai Maksimal: ", bil[-1])
