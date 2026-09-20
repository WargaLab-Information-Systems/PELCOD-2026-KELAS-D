
angka_1 = 125
angka_2 = 60
hasil = angka_1 // angka_2
print("Hasil pembagian integer:", hasil)

tinggi = 1.70
berat = 50
IMT = berat / (tinggi ** 2)
if IMT < 18.5:
    print('Kurus')
elif IMT >= 18.5 and IMT < 25:
    print('Normal')
elif IMT >= 25 and IMT < 30:
    print('Gemuk')
else:
    print('Obesitas')