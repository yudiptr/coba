# Menetapkan variable
nama_a = input('Masukkan input himpunan A: ')
nama_b = input('Masukkan input himpunan B: ')
hasil = list()
hasil1 = list()
koma_a = -1
koma_b = -1

# Membuat for loop untuk mencari index dari koma
# Enumerate untuk mencari index koma lalu dimasukkan ke hasil
for mbe, value in enumerate(nama_a):
    if value == ',':
        hasil.append(mbe)
        
for mba, value in enumerate(nama_b):
    if value == ',':
        hasil1.append(mba)

print('A', 'x', 'B', '= { ',end='' )

# Membuat for loop untuk mencetak kalimat
# Dari index awal hingga index sebelum koma
for i_a in range (len(hasil)):
    for i_b in range (len(hasil1)):
        print('(' + nama_a[koma_a + 1 : int(hasil[i_a])] +  ',',end='')
        print(nama_b[koma_b + 1 : int(hasil1[i_b])] +  '), ',end='')
        koma_b = hasil1[i_b]
    else :
        print('(' + nama_a[koma_a + 1 : int(hasil[i_a])] +  ',',end='')
        print(nama_b[int(hasil1[i_b]) + 1 : ] +  '), ',end='')
    koma_a = int(hasil[i_a])
    koma_b = -1
# Membuat syarat agar tetap mengprint kata setelah last coma
else : 
    for i_b in range (len(hasil1)):
        print('(' + nama_a[int(hasil[i_a]) + 1 : ] +  ',',end='')
        print(nama_b[koma_b + 1 : int(hasil1[i_b])] +  '), ',end='')
        koma_b = hasil1[i_b]
    else :
        print('(' + nama_a[int(hasil[i_a]) + 1 : ] +  ',',end='')
        print(nama_b[int(hasil1[i_b]) + 1 : ] +  ')', end='')
        
print(' }')