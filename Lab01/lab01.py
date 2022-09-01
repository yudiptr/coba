# Mengimport math untuk mengambil value pi
import math

print('==' * 30 )

# Memberi input untuk user memasukkan nilai radius 
# Lalu mengonvert menjadi float
radius = float(input('Masukkan radius lingkaran berupa angka : '))

# Membuat input validations (Ide dari Bryan Naufal)
# Membuat syarat jika radius < 0, maka user akan diminta memasukkan
# radius yang > 0
if radius < 0 : 
    print("Harap masukkan radius yang lebih besar dari 0")

# Membuat syarat jika radius >=, maka program akan bekerja
# Membuat formula untuk mencari luas daerah di dalam variabel
elif radius >= 0 :
    red_area =  (4 * radius ** 2 ) - ( math.pi * radius ** 2)
    yellow_area = (math.pi * radius ** 2) - (radius ** 2)
    purple_area = radius ** 2

    # Mencetak hasil dari masing-masing area
    # Mengubah nilai dari red, yellow, dan purple menjadi string 
    # agar dapat melakukan operasi +.
    # Mengambil 2 digit di belakang koma
    print('Luas daerah cat merah     : ' + str('{:.2f}'.format(red_area)))
    print('Luas daerah cat kuning    : ' + str('{:.2f}'.format(yellow_area)))
    print('Luas daerah cat ungu      : ' + str('{:.2f}'.format(purple_area)))
    print('==' * 30 )


# mengambil 2 angka dibelakang koma : https://www.pythonindo.com/pemformatan-di-python/