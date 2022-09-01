open_file = input('Masukkan nama file percakapan : ') 
print()
try : # Try n check wether the file exist r not
    file = open(open_file, 'r', encoding='utf-8')
    read = file.readlines()
    temp = list()
    if read == []: # Making exception for file exist but zonk
        print('File input ada tapi kosong :(')
    else :
        # Set Variable 
        happiness = 50
        sadness = 50
        anger = 50

        def f_smile(): # Function to calculate happiness
            global happiness, sadness
            happiness +=  9
            sadness -=  6
            if happiness > 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0
            if sadness > 100:
                sadness = 100
            elif sadness < 0:
                sadness = 0
        def f_sad(): # Function to calculate sad
            global sadness, anger
            sadness +=  10
            anger -=  8
            if sadness > 100:
                sadness = 100
            elif sadness < 0:
                sadness = 0
            if anger > 100 :
                anger = 100
            elif anger < 0:
                anger = 0
        def f_angry(): # Function to calculate anger
            global happiness, anger
            anger += 13
            happiness -= 5
            if happiness > 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0
            if anger > 100 :
                anger = 100
            elif anger < 0:
                anger = 0
        for lst in  range (len(read)): # Iterate every line
            mid = read[lst].split(' ') # Split every line per word
            for next_mid in mid: # Iterate per word for each line
                # Check the emoji
                a = next_mid
                if a == '\n':
                    temp.append('')
                elif a == '(smile)' or a == '(smile)\n':
                    temp.append('\U0001f603')
                    if mid[0] == 'Pak':
                        f_smile()
                elif a == '(sad)' or a == '(sad)\n':
                    temp.append('\U0001f622')
                    if mid[0] == 'Pak':
                        f_sad()
                elif a == '(angry)' or a == '(angry)\n':
                    temp.append('\U0001f621')
                    if mid[0] == 'Pak':
                        f_angry()
                else :
                    temp.append(a)
            temp.append('\n')

        def result(): # Function to check final condition
            global happiness, sadness, anger
            if happiness == sadness == anger:
                return 'Kesimpulan tidak ditemukan'
            elif happiness == sadness :
                return 'Pak Chanek sedang bahagia atau sedih'
            elif happiness == anger :
                return 'Pak Chanek sedang bahagia atau marah'
            elif sadness == anger :
                return 'Pak Chanek sedang sedih atau marah'
            elif sadness < happiness > anger :
                return 'Pak Chanek sedang bahagia'
            elif happiness < sadness > anger : 
                return 'Pak Chanek sedang sedih'
            else :
                return 'Pak Channek sedang marah'

        for hasil_akhir in temp:
            if hasil_akhir == '\n':
                print(hasil_akhir, end='')
            else :
                print(hasil_akhir, end=' ')
        # Print result
        print()
        print(f"Mengukur suasana hati....")
        print()
        print("##### Hasil Pengukuran #####")
        print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
        print()
        print("##### Kesimpulan #####")
        print(f'{result()}')
except FileNotFoundError : # If file doesn't exist, run this
    print('File input tidak ada :(')