class_train = {'Eksekutif':1, 'Bisnis':2, 'Ekonomi':3} # Buat dict untuk get class
print('Selamat datang! Silakan masukkan jadwal KA : ')
ask = input()
target = list()

while ask.lower() != 'selesai': # ketika input tidak = selesai, minta lagi
    temp = ask.split()
    if len(temp) == 4 : # validasi input biar yang masuk cuma 4 kata (no tujuan jam harga)
        target.append(temp)
    ask = input()

destination = list()
number = list()
price = list()
hour = list()

for a in target: # Separating in each category
    destination.append(a[1])
    hour.append(a[2])
    price.append(a[3])
    number.append(a[0])

print('''
Perintah yang tersedia:
1. INFO_TUJUAN
2. TUJUAN_KELAS <tujuan_akhir> <kelas_kereta>
3. TUJUAN_KELAS_TERMURAH <tujuan_akhir> <kelas_kereta>
4. TUJUAN_JAM <tujuan_akhir> <jam_keberangkatan>
5. TUJUAN_JAM_TERMURAH <tujuan_akhir> <jam_keberangkatan>
6. EXIT''')

command = ''
def ask_input(): # Function for asking command
    print()
    global command
    command = input('Masukkan perintah : ')
    if command == 'INFO_TUJUAN':
        info_tujuan()
    elif (len(command.split()) == 3) and (command[:13] == 'TUJUAN_KELAS '):
        tujuan_kelas()
    elif (len(command.split()) == 3) and (command[:21] == 'TUJUAN_KELAS_TERMURAH'):
        cheapest_tujuan_kelas()
    elif (len(command.split()) == 3) and (command[:11] == 'TUJUAN_JAM '):
        tujuan_jam()
    elif (len(command.split()) == 3) and (command[:19] == 'TUJUAN_JAM_TERMURAH'):
        cheapest_tujuan_jam()
    elif command == 'EXIT': # If user input == exit, program end
        print('Terima kasih sudah menggunakan program ini!')
        exit()
    else : 
        print('Perintah yang dimasukkan tidak valid.')
        ask_input() # If input out of range, print invalid and ask command again

def info_tujuan(): # If user want to know dest only
    dest_only = set(destination) # Make dest into set to prevent double dest in console
    if len(dest_only) : # Validating if destination is exist
        print('KA di stasiun ini memiliki tujuan akhir :')
        for a in dest_only :
            print(a)
        ask_input()
    else :
        print('Hari ini tidak ada jadwal :D')
        ask_input()

def tujuan_kelas():
    global command
    info_command = command.split()
    hasil = list()
    final = list()
    counter = 0 # Validating input if nothing is printed, jadwal isn't exist
    if info_command[2] in ['Ekonomi', 'Bisnis', 'Eksekutif']: # Validating wether Class in the list
        a = class_train.get(info_command[2])
        for key,value in enumerate(number): # Get all index which is included in command
            if int(a) == int(value[0]):
                hasil.append(key)
        for a in hasil: # Get entire information of train if index is found
            if info_command[1] == destination[a]:
                final.append([destination[a], hour[a], number[a], price[a]])
                counter += 1
        if counter :
            if len(final) :
                for a in final:
                    print(f"KA {a[2]} berangkat pukul {a[1]} dengan harga tiket {a[3]}")
                ask_input()
            else : # If nothing in final, it means destination isn't exit
                print('Tidak ada jadwal KA yang sesuai.')
                ask_input()
        else : # If counter == 0, it means destination isn't exit
            print('Tidak ada jadwal KA yang sesuai.')
            ask_input()
    else : # If input out of class_train, invalid
        print('Perintah yang dimasukkan tidak valid')
        ask_input()

def tujuan_jam():
    global command
    info_command = command.split()
    hasil = list()
    final = list()
    try : # Make sure the time isdigit
        patokan = int(info_command[2])
        for a,value in enumerate(destination): # Find index destination as user want
            if value == info_command[1] : # Make sure dest is same
                hasil.append(a)
        for b in hasil:
            temp_hour = hour[b]
            if int(temp_hour) <= patokan: # Get entire information for time < the time which user asked 
                final.append([destination[b], temp_hour, number[b], price[b]])
    except ValueError: # If time is not digit, run this
        print('Perintah yang dimasukkan tidak valid')
        ask_input()
    else : # If nothing error, run this 
        if len(final) :
            for a in final:
                print(f"KA {a[2]} berangkat pukul {a[1]} dengan harga tiket {a[3]}")
        else : print('Tidak ada jadwal KA yang sesuai.') # If final == 0, destination isn't exit.
        ask_input() # loop for asking command again

def cheapest_tujuan_kelas(): # If user want chepest_dest_class
    global command
    info_command = command.split()
    hasil = list()

    if (info_command[2] in ['Ekonomi', 'Bisnis', 'Eksekutif']):
        a = class_train.get(info_command[2])

        for key,value in enumerate(number):
            if (int(a) == int(str(value[0]))) and (info_command[1] == destination[key]):
                hasil.append(key) # Get entire index for number as input wants
        
        temp_harga = [int(price[a]) for a in (hasil)] 
        if hasil  : # If anything in hasil, destination is exitst
            fixed_price = min(temp_harga) # Looking for minimum price
            for a in hasil:
                b = target[a] # Get specified info from target based on index in hasil
                if b[1] == info_command[1]: # Validation if destination is as user want
                    if str(fixed_price) in b : # Check if the minimum price is exist in specified target
                        print(f"KA {b[0]} berangkat pukul {b[2]} dengan harga tiket {b[3]}")
            ask_input()
        else : # If nothing in hasil, destination isn't exist
            print('Tidak ada jadwal KA yang sesuai.')
            ask_input()
    else : # If the class which is user inputed is not in the list
        print('Perintah yang dimasukkan tidak valid')
        ask_input()

def cheapest_tujuan_jam(): # If the user want
    global command
    global target
    info_command = command.split()
    hasil  = list()
    price = list()
    try :  # Make sure the time isdigit
        a = int(info_command[2])
        if target :
            for b in target :
                if (int(b[2]) <= a) and (info_command[1] == b[1]): # Validating destination is same
                    hasil.append([b[3],b[2],b[1],b[0]]) # and time is < than user input
                    price.append(int(b[3])) # Get the price
        else : # Nothing in target == destination is not exist
            print('Tidak ada jadwal KA yang sesuai') 
            ask_input()
    except ValueError: # If time is not digit, run this
        print('Perintah yang dimasukkan tidak valid')
        ask_input()
    else : # If nothing error, run this 
        if hasil:
            price_fixed = min(price) # Get the minimum price
            for a in hasil:
                if str(price_fixed) in a:
                    print(f"KA {a[3]} berangkat pukul {a[1]} dengan harga tiket {a[0]}")
            ask_input()
        else : # Nothing in hasil -> destination is not exit
            print('Tidak ada jadwal KA yang sesuai')    
            ask_input()
ask_input() # Start