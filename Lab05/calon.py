open_file = input('Masukkan nama file percakapan : ') 
print()
print()
try : # Try n check wether the file exist r not
    file = open(open_file, 'r')
    read = file.readlines()
    temp = list()
    if read == []: # Making exception for file exist but zonk
        print('File input ada tapi kosong :(')
    else :
        # Set Variable
        smile = 0
        sad = 0
        angry = 0
            
        happiness = 50
        sadness = 50
        anger = 50

        def f_smile(): # Function to calculate happiness
            global smile, happiness, sadness, anger, sad, angry
            happiness += smile * 9
            sadness -= smile * 6
            if happiness > 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0
            if sadness > 100:
                sadness = 100
            elif sadness < 0:
                sadness = 0
            if anger > 100 :
                anger = 100
            elif anger < 0:
                anger = 0
            smile = 0
            sad = 0
            angry = 0
        def f_sad(): # Function to calculate sad
            global smile, happiness, sadness, anger, sad, angry
            sadness += sad * 10
            anger -= sad * 8
            if happiness > 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0
            if sadness > 100:
                sadness = 100
            elif sadness < 0:
                sadness = 0
            if anger > 100 :
                anger = 100
            elif anger < 0:
                anger = 0
            smile = 0
            sad = 0
            angry = 0
        def f_angry(): # Function to calculate anger
            global smile, happiness, sadness, anger, sad, angry
            anger += angry * 13
            happiness -= angry * 5
            if happiness > 100:
                happiness = 100
            elif happiness < 0:
                happiness = 0
            if sadness > 100:
                sadness = 100
            elif sadness < 0:
                sadness = 0
            if anger > 100 :
                anger = 100
            elif anger < 0:
                anger = 0
            smile = 0
            sad = 0
            angry = 0
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
                        smile += 1
                        f_smile()
                elif a == '(sad)' or a == '(sad)\n':
                    temp.append('\U0001f622')
                    if mid[0] == 'Pak':
                        sad += 1
                        f_sad()
                elif a == '(angry)' or a == '(angry)\n':
                    temp.append('\U0001f621')
                    if mid[0] == 'Pak':
                        angry += 1
                        f_angry()
                else :
                    temp.append(a)
            temp.append('\n')

        def result(): # Function to check final condition
            global happiness, sadness, anger
            if happiness == sadness == anger:
                return 'Kesimpulan tidak dapat ditemukan'
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

        for a in temp:
            if a == '\n':
                print(a,end='')
            else :
                print(a, end=' ')
        # Print result
        print()
        print()
        print(f"Mengukur suasana hati....")
        print()
        print()
        print("##### Hasil Pengukuran #####")
        print(f"Happiness = {happiness} | Sadness = {sadness} | Anger = {anger}")
        print()
        print()
        print("##### Kesimpulan #####")
        print(f'{result()}')
except FileNotFoundError : # If file doesn't exist, run this
    print('File input tidak ada :(')