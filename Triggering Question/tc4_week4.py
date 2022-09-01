# 4.1
name = input('Masukkan kata : ')
character = input('Masukkan karakter yang ingin dikapitalisasi : ')
print('Hasil akhir : ', end='')
for a in name :
    if a == character :
        print(a.capitalize(), end='')
    else :
        print(a, end='')

 # 4.2
name = input('Masukkan kata : ')
baru = ''
for a in name :
    if a.islower():
        a = a.replace(a, a.upper())
    elif a.isupper() : 
        a = a.replace(a, a.lower())
    baru += a
print(baru)

# 3.2
i = input('Masukkan kata : ')
a = i.split()
for b in a[::-1]:
    print(b, end=' ')