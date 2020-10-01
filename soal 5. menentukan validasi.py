"""
Created on Oct 01 2020

@author: 190411100031/Nur Mu'izzul Qodir
"""
print("Program untuk menentukan validasi username dan password")

kondisi = True
coba = 0
data = ['izzul','katasandi']
while kondisi:
    username = input("Username: ")
    password = input("Password: ")
    if username == data[0] and password == data[1]:
        print("Anda Berhasil Masuk")
        kondisi = False
    else:
        print("Maaf Username dan Password Anda Salah")
        coba += 1
        if coba >= 3:
            print("Maaf Anda Sudah Gagal 3x Login Program di Hentikan")
            break
