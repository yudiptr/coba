day_h = 60 * 24
hour_h = 60

lis_day = {
    0:'Senin', 1:'Selasa', 2:'Rabu', 3:'Kamis',
    4:'Jumat', 5:'Sabtu', 6:'Minggu'} # Make dictionary for days

day = [i * day_h for i in range (7)] # Make list of days in form of number
hour = [i * hour_h for i in range (24)]

# Make variable only name, start, and end time
data = list()
matkul_only = list()
start_only = list()
end_only = list()

MATKUL_TERSEDIA = [
["ddp 1 A ",     day[0] + hour[8] + 0,    day[0] +  hour[9] + 40],
["ddp 1 a ",     day[2] + hour[8] + 0,    day[2] +  hour[9] + 40],
["ddp 1 a     ",     day[3] + hour[8] + 0,    day[3] +  hour[9] + 40],
["ddp 1 b",     day[1] + hour[8] + 0,    day[1] +  hour[9] + 40],
["maNbis",      day[0] + hour[9] + 0,    day[0] + hour[10] + 40],
["matdis 1 a",  day[2] + hour[9] + 0,    day[2] + hour[10] + 40],
["matdis 1 b",  day[0] + hour[9] + 0,    day[0] + hour[10] + 40]
]

for a in range (len(MATKUL_TERSEDIA)): # Iterate every list in matkul tersedia and append in into specific list
    matkul_only.append(MATKUL_TERSEDIA[a][0].strip().lower())
    start_only.append(MATKUL_TERSEDIA[a][1])
    end_only.append(MATKUL_TERSEDIA[a][2])

def intro(): # Make intro for asking which menu the user want to use
    print('''=========== SUSUN JADWAL ===========
1  Add matkul
2  Drop matkul
3  Cek ringkasan
4  Lihat daftar matkul 
5  Selesai 
====================================
''')
    choose = input('Masukkan pilihan : ')
    if choose == '1':
        add_matkul()
    elif choose == '2':
        drop_matkul()
    elif choose == '3':
        cek_ringkasan()
    elif choose == '4' :
        list_matkul()
    elif choose == '5':
        print('Terima kasih!')
        quit()
    else : # Make exception if input out of range and ask the input again
        print('Maaf, pilihan tidak tersedia')
        intro()

def add_matkul(): # If user want to add matkul, this function will run
    global data
    option = input('Masukkan nama matkul : ')
    temp = option.lower().split()
    option_fix = str()
    for a in temp:
        option_fix += a + ' '
    hasil = list()
    bin = 0
    if option_fix[:-1] in matkul_only: # Check whether the matkul exist or not (case insensitive)
        for a, value in enumerate(matkul_only): # Find if there is matkul which has 2 schedule in a week
            if value == option_fix[:-1]:
                hasil.extend([a]) # Add the index of the matkul
        kosong = [[option_fix[:-1], start_only[a], end_only[a]] for a in hasil]
        for a in kosong: # Make exception if matkul hasn't been added, then it will be added
            if not (a in data): 
                data.extend([a])
                bin += 1
        if not bin : print('Matkul sudah pernah anda masukkan') # If matkul exist in added list, print this
    else : print('Matkul tidak ditemukan')  # If matkul doesnt exist in MATKUL_TERSEDIA, print this
    print()
    intro()

def drop_matkul(): # If user want to drop matkul, this function will run
    global data
    temp = 0
    temp_data = []
    option = input('Masukkan nama matkul : ')
    temp_fix = option.lower().split()
    option_fix = str()
    for a in temp_fix:
        option_fix += a + ' '
    for a in data: # Find if the matkul exist in data, it will be listed on temp_data
        if option_fix[:-1] in a :
            temp_data.append(a)
            temp += 1
    if temp == 0 : print('Matkul tidak ditemukan') # If matkul doesnt exist in data, print this
    else :
        for a in temp_data: # Remove the data which is listed in temp_data
            data.remove(a)
    print()
    intro()

def cek_ringkasan(): # If user want to check summary, run this
    global data
    temp = 0
    nest_data = list()
    for a in data: # Iterate every list in data
        for b in data: 
            if a != b : # Make sure the iterated one is not the same data
                if b[1] in range(a[1],a[2]): # If the scedule in range of other matkul schedule, it's bentrok
                    temp += 1
                    c = sorted((a[0], b[0])) # To make (a,b) and (b,a) is counted as the same and will not be double list
                    if not (c in nest_data):
                        nest_data.append(c) # If matkul doesnt exist in nest_data, it will be append on it.
                    else :
                         continue
            else:
                continue
    if not temp: # If temp == 0 (Nothing error), run this
        print('Tidak ada mata kuliah yang bermasalah')
    else : # If temp != 0, run this to print the bentrok one
        for a in sorted(nest_data):
            print(' ', a[0].upper(), 'bentrok dengan', a[1].upper())
    print()
    intro()

def list_matkul(): # If user want to see the matkul, run this
    sort_data = sorted(data) # Sort matkul alphabetically
    if len(sort_data) == 0 : 
        print('Tidak ada mata kuliah yang diambil')
    else :
        for a in sort_data:
            day = ((a[1] // (24*60)) % 7, (a[2] // (24*60)%7))  # To get the days
            hour = ((a[1] // (60) % 24), (a[2] // (60))%24) # To get the hour
            minute = ((a[1] % 60), (a[2]%60)) # To get the minute
            # Take the day from the dict on the header using result from day
            print(f"""    {a[0].upper():<15}{lis_day[day[0]]+',':<10s}{hour[0]:02d}.{minute[0]:02d}\
 s/d {lis_day[day[1]] +',':<10s}{hour[1]:02d}.{minute[1]:02d}  """)
    print()
    intro()

intro() # Run intro as the first activity