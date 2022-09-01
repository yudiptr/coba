# Meminta jumlah mata kuliah dari user
import sys
print('Selamat datang di Kalkulator IPK!')
print('=====' * 10)
sks = int(input('Masukkan jumlah mata kuliah : '))
print('=====' * 10)

# Membuat syarat agar input yang diberikan user > 0
if sks == 0 :
    print("Tidak ada mata kuliah yang diambil")
    sys.exit()
while sks < 0 :
    sks = int(input('Masukkan jumlah mata kuliah : '))

# Membuat variabel penampung hasil perhitungan yang lulus dan total
sks_lulus = 0
sks_sum = 0
temp_mutu_lulus = 0
temp_mutu_tot = 0

# Membuat loop untuk meminta user menginput data pelajaran
for matkul in range (1, sks + 1) : 
    nama_matkul = input('Masukkan nama mata kuliah ke-' + str(matkul) + ' : ')
    total_sks = int(input('Masukkan jumlah SKS ' + nama_matkul + ': '))
    # Mengecek input total SKS
    while total_sks < 0 :
        print('Harap masukkan jumlah SKS yang benar! ')
        total_sks = int(input('Masukkan jumlah SKS ' + nama_matkul + ': '))
    total_score = float(input('Masukkan nilai yang kamu dapatkan: '))

    # Mengecek input nilai
    while total_score < 0 :
        print('Nilai yang kamu masukkan tidak valid')
        total_score = float(input('Masukkan nilai yang kamu dapatkan: '))
    print('=====' * 10)

    # Membuat kriteria penilaian
    if total_score >= 0 : 
        if total_score >= 85 :
            bobot = 4.00
            keterangan = 'Lulus'
        elif 80 <= total_score < 85 :
            bobot = 3.70
            keterangan = 'Lulus'
        elif 75 <= total_score < 80 :
            bobot = 3.30
            keterangan = 'Lulus'
        elif 70 <= total_score < 75 :
            bobot = 3.00
            keterangan = 'Lulus'
        elif 65 <= total_score < 70 :
            bobot = 2.70
            keterangan = 'Lulus'
        elif 60 <= total_score < 65 :
            bobot = 2.30
            keterangan = 'Lulus'
        elif 55 <= total_score < 60 :
            bobot = 2.00
            keterangan = 'Lulus'
        elif 40 <= total_score < 55 :
            bobot = 1.00
            keterangan = 'Tidak Lulus'
        elif 0 <= total_score < 40 :
            bobot = 0.00
            keterangan = 'Tidak Lulus'
    # Menghitung ip berdasarkan input
    mutu = bobot * total_sks
    sks_sum += total_sks
    temp_mutu_tot += mutu

    # Membuat ketentuan untuk matkul yang lulus
    if keterangan == 'Lulus' : 
        sks_lulus += total_sks
        temp_mutu_lulus += mutu

# Membuat ketentuan jika sks_lulus > 0, dilakukan perhitungan normal
if sks_lulus > 0 :
    ipk_total = f"{(temp_mutu_lulus / sks_lulus):.2f}"
    ipt_total = f"{((temp_mutu_tot) / (sks_sum)):.2f}"
    print('Jumlah SKS Lulus :', sks_lulus, '/', sks_sum)
    print('Jumlah mutu lulus :', f"{temp_mutu_lulus:.2f}", '/', f"{(temp_mutu_tot):.2f}")
    print('Total IPK kamu adalah :', ipk_total)
    print('Total IPT kamu adalah :', ipt_total)

# Membuat ketentukan jika sks_lulus < 0 dan sks input = 0
# untuk menhindari divided by zero
elif sks_lulus == 0 :
    if sks_sum == 0:
        print('Jumlah SKS Lulus :', sks_lulus, '/', sks_sum)
        print('Jumlah mutu lulus :', f"{temp_mutu_lulus:.2f}", '/', f"{(temp_mutu_tot):.2f}")
        print('Total IPK kamu adalah : 0.00')
        print('Total IPT kamu adalah : 0')
    else : 
        print('Total IPT kamu adalah :', f"{((temp_mutu_tot) / (sks_sum)):.2f}")
        print('Jumlah SKS Lulus :', sks_lulus, '/', sks_sum)
        print('Jumlah mutu lulus :', f"{temp_mutu_lulus:.2f}", '/', f"{(temp_mutu_tot):.2f}")
        print('Total IPK kamu adalah : 0.00')
