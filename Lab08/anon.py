print('Masukkan rantai penyebaran : ')
rantai = input()
ppl_rantai = list()
perintah = ''
valid = list()
sus_kopit = list()
dummy_sus = list()
while rantai != 'selesai' :
    b = rantai.split()
    if len(b):
        ppl_rantai.extend([b])
    rantai = input()

ppl = set()
for i in ppl_rantai:
    for j in i:
        ppl.add(j)

print('''\nList perintah:\n1. RANTAI_PENYEBARAN
2. CEK_PENULARAN \n3. EXIT''')

def rantai_penyebaran(name):
    global sus_kopit, dummy_sus, valid
    in_perintah = perintah.split()
    index_0 = list(name[0])
    index_host = ppl_rantai.index(index_0)
    if in_perintah[1] in ppl:

        if index_0[0] == in_perintah[1]:
            sus_kopit = [i for i in index_0 if not(i in sus_kopit)]
            dummy_sus = sus_kopit.copy()
            next_rantai(ppl_rantai[index_host+1:])
        else :
            if len(name[1:]) > 1:
                rantai_penyebaran(name[1:])
            else : dummy_sus.append(in_perintah[1])
    else :
        print(f"Maaf, nama {in_perintah[1]} tidak ada dalam rantai penyebaran.")

def next_rantai(name):
    global sus_kopit, dummy_sus
    index_0 = list(name[0])
    for a in sus_kopit:
        if a in index_0:
            dummy_sus.extend([i for i in index_0 if not(i in dummy_sus)])

    if len(name[1:]):
        next_rantai(name[1:])
    else : 
        pass

def cek_penularan():
    global perintah, valid, dummy_sus
    fixed_ppl = list()
    for a in ppl_rantai:
        for b in a :
            if b not in fixed_ppl:
                fixed_ppl.append(b)

    in_perintah = perintah.split()
    if (in_perintah[1] in fixed_ppl) and (in_perintah[2] in fixed_ppl):
        perintah = f"RANTAI_PENYEBARAN {in_perintah[2]}"
        rantai_penyebaran(ppl_rantai)
        if (in_perintah[1] in dummy_sus) and (in_perintah[2] in dummy_sus):
            if dummy_sus.index(in_perintah[1]) >= dummy_sus.index(in_perintah[2]):
                print('YA')
            else : 
                print('TIDAK')
            sus_kopit.clear()
            dummy_sus.clear()
        else : print('TIDAK')
    elif (in_perintah[1] not in fixed_ppl) and (in_perintah[2] in fixed_ppl):
        print(f"Maaf, nama {in_perintah[1]} tidak ada dalam rantai penyebaran.")
    elif (in_perintah[1] in fixed_ppl) and (in_perintah[2] not in fixed_ppl):
        print(f"Maaf, nama {in_perintah[2]} tidak ada dalam rantai penyebaran.")
    elif (in_perintah[1] not in fixed_ppl) and (in_perintah[2] not in fixed_ppl):
        print(f"Maaf, nama {in_perintah[1]} dan {in_perintah[2]} tidak ada dalam rantai penyebaran.")

while True:
    print()
    perintah = input('Masukkan perintah : ')
    in_perintah = perintah.split()
    if (len(in_perintah) == 2) and (in_perintah[0]+ ' ' == 'RANTAI_PENYEBARAN '):
        rantai_penyebaran(ppl_rantai)
        if dummy_sus:
            print(f"Rantai penyebaran {in_perintah[1]}:")
            for a in dummy_sus:
                print(f"- {a}")
            dummy_sus.clear()
            sus_kopit.clear()
    elif (len(in_perintah) == 3) and (in_perintah[0]+ ' ' == 'CEK_PENULARAN '):
        cek_penularan()
    elif perintah == 'EXIT':
        print('Goodbye~ Semoga virus KOPIT cepat berakhir.')
        exit()
    else : print('Maaf perintah tidak dikenali. Masukkan perintah yang valid.')