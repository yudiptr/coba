print('Masukkan rantai penyebaran : ')
chain = input()
name_list = list()
command = ''
temp_kopit = list()
all_name = list()

while chain != 'selesai' : # Validating input wheter it is selesai or not
    info_chain = chain.split()
    if len(info_chain):
        name_list.append(info_chain)
    chain = input() # looping again until input is seelsai

for i in name_list: # get all name from input
    for j in i:
        if j not in all_name:
            all_name.append(j)

print('''
List perintah:\n1. RANTAI_PENYEBARAN
2. CEK_PENULARAN \n3. EXIT''')

def ask(): # As a starting to ask the command
    global command
    print()
    command = input('Masukkan perintah : ')
    if (len(command.split()) == 2) and (command[:18] == 'RANTAI_PENYEBARAN '):
        rantai_penyebaran(name_list)
        info_command = command.split()
        print(f"Rantai penyebaran {info_command[1]}:")
        for a in temp_kopit:
            print(f"- {a}")
        temp_kopit.clear() # clear the temp_kopit variable
        ask()
    elif (len(command.split()) == 3) and (command[:14] == 'CEK_PENULARAN '):
        cek_penularan()
        ask()
    elif command == 'EXIT':
        print('Goodbye~ Semoga virus KOPIT cepat berakhir.')
        quit()
    else : # Validating command if the command is out of the range
        print('Maaf perintah tidak dikenali. Masukkan perintah yang valid.')
        ask()

def rantai_penyebaran(lst):
    global temp_kopit
    info_command = command.split()
    first_index = list(lst[0]) # Get the first index from list for recursion
    if info_command[1] in all_name: # Validating input wheter the name in in the list or not
        if info_command[1] == first_index[0]: # Checking the the input as a kopit_host
            for a in first_index: # Get the entire name on first index and append it into list
                if a not in temp_kopit:
                    temp_kopit.append(a)
            find_index = name_list.index(first_index)
            if len(lst[1:]) > 1: # Checking the carrier from the host
                cek_chain(name_list[find_index+1:])
            else :
                pass
        else : 
            if len(lst[1:]) > 1: # Validating for recursion
                rantai_penyebaran(lst[1:])
            else : # If it's the end of name_list and it has the same value as input, run this
                if not(len(temp_kopit)):
                    temp_kopit.append(info_command[1])
    else : # If the name is not in the list, run this
        print(f"Maaf, nama {info_command[1]} tidak ada dalam rantai penyebaran.")
        ask()

def cek_chain(temp_nama): # If the host is found, it will run
    global temp_kopit
    first_index = list(temp_nama[0])
    if len(temp_nama):
        nest_temp_kopit = list()
        for b in temp_kopit: # Getting the suspect from carrier
            if b in first_index:
                for i in first_index:
                    if i not in temp_kopit: # Validating to prevent double name in list
                        nest_temp_kopit.append(i)
        for a in nest_temp_kopit:
            temp_kopit.append(a)
        if len(temp_nama[1:]) > 1 : # Validating for recursion if it's not the end list
            cek_chain(temp_nama[1:])

def cek_penularan(): # For cek_penularan, run this
    global command
    info_command = command.split()
    cek_name1, cek_name2 = info_command[1],info_command[2] # Getting the carrier, host
    name1 = cek_name1 in all_name # Check the name wheter it's on the list
    name2 = cek_name2 in all_name
    checker = f"{name1} and {name2}"
    if (cek_name1 in all_name) and (cek_name2 in all_name):
        command = f'RANTAI_PENYEBARAN {info_command[2]}'
        info_command = command.split() # Check the carrier from the host in check penularan
        rantai_penyebaran(name_list)
        # Validating wheter the name is in the host and carrier list
        if (cek_name1 in temp_kopit) and (cek_name2 in temp_kopit): 
            # If the index host < carrier, it means the carrier is being infected indirectly
            if temp_kopit.index(cek_name1) >= temp_kopit.index(cek_name2):
                print('YA')
            else : print('TIDAK')
        else : print('TIDAK')
        temp_kopit.clear()
    elif checker == 'False and True': # Validating the name
        print(f"Maaf, nama {cek_name1} tidak ada dalam rantai penyebaran.")
    elif checker == 'True and False':
        print(f"Maaf, nama {cek_name2} tidak ada dalam rantai penyebaran.")
    else : print(f"Maaf, nama {cek_name1} dan {cek_name2} tidak ada dalam rantai penyebaran.")
ask() # Start asking for command