a = input('Masukkan A : ')
b = input('Masukkan B : ')
a_baru = a + ','
b_baru = b + ','
koma_a = -1
koma_b = -1
hasil = ''
print( 'A x B = { ',end='')
for wa in range (len(a_baru)):
    if a_baru[wa] == ',':
        for wab in range(len(b_baru)):
            if b_baru[wab] == ',':
                hasil += f'({a_baru[koma_a + 1:wa]}, {b_baru[koma_b+1:wab]}), '
                koma_b = wab       
        
        koma_b = -1
        koma_a = wa
print(hasil[:-2],end='')
print(' }')