import random # Import random for choose random int
print('===' * 15)
print("Halo, selamat datang di Mathbot")

# Variable to be accessed globally
quiz = 'Pilih kuis:\n1. Kuis Lepas\n2. Kuis 5\n3. Ganti mode\n4. Akhiri program'
select_mode = ''
select_quiz = ''
score = 0
 
def choose(): # Choose the mode 
    if select_mode == '1' :
        print('Baik, pilih mode penjumlahan ya, sekarang pilih jenis kuis apa?')
        mode_penjumlahan_1() 
    elif select_mode == '2' :
        print('Baik, pilih mode pengurangan ya, sekarang pilih jenis kuis apa?')
        mode_pengurangan_1() 
    elif select_mode == '3' :
        print('Baik, pilih mode campur ya, sekarang pilih jenis kuis apa?')
        mode_campur() 
    elif select_mode == '4' :
        print('Terima kasih telah bermain kuis ini. Sampai jumpa lagi!')
        quit() # end the program when the input = 4
    else : 
        print('''Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.''')
        print('===' * 15)
        intro() # when the input of mode is out of range, program restart to the main menu
        
def intro(): # Trigger the intro when the program is started
    global select_mode 
    mode = 'Pilih Mode:\n1. Penjumlahan\n2. Pengurangan\n3. Campur\n4. Akhiri Program'
    print(mode)
    print()
    print()
    select_mode = input('Masukkan perintah : ')
    print('===' * 15)
    choose() # Trigger the function to the selected mode

def rumus_jumlah(): # Addition formula
    global select_quiz
    global score
    a = random.randint(0,10)
    b = random.randint(0,10)
    print('Berapa', a, '+', b, '?')
    answer = input('Jawab : ')
    if select_quiz == '1' and answer == 'akhiri kuis':
        print('===' * 15)
        mode_penjumlahan_1()
    
    elif answer.strip('-').isnumeric(): # Check wether the input is numeric or not
        if answer == str(a + b) :
            print('Hore benar!')
            print('===' * 15)
            score += 20
        elif answer != str(a + b) : 
            print('Masih kurang tepat, ya. Jawabannya adalah', a + b)
            print('===' * 15)
    else : #If the answer is out of range, print below
        print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.')
        print('===' * 15)
    
def mode_penjumlahan_1(): # Function to trigger the addition formula
    while True :
        global score
        global select_quiz
        print(quiz)
        print()
        print()
        select_quiz = input('Masukkan jenis kuis: ') 
        print('===' * 15)
        if select_quiz.isnumeric():
            if int(select_quiz) == 1 : 
                while True : # The program will not end until user ask it
                    rumus_jumlah()        

            elif int(select_quiz) == 2 :
                score = 0
                for quiz_5 in range (1,6): # Making loop for trigger 5 question
                    print('Pertanyaan ke' , quiz_5, ': ', end='')
                    rumus_jumlah()
                print('Score kamu : ', score)
                print('===' * 15)
                score = 0
                continue
            elif int(select_quiz) == 3 : 
                intro()
            elif int(select_quiz) == 4 :
                print('Terima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                quit() # quiz the program if user input 4
            else :
                print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
                print('===' * 15)
                continue # retrigger this function if answer out of range
        else :
            print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
            print('===' * 15)
            continue
                
def rumus_kurang() : # Substraction formula
    global select_quiz
    global score
    a = random.randint(0,10)
    b = random.randint(0,a)
    print('Berapa', a, '-', b, '?')
    answer = input('Jawab : ')
    if select_quiz == '1' and answer == 'akhiri kuis' :
        print('===' * 15)
        mode_pengurangan_1()
    elif answer.strip('-').isnumeric():
        if int(answer) == a - b :
            print('Hore benar!')
            print('===' * 15)
            score += 20
        elif int(answer) != a - b : 
            print('Masih kurang tepat, ya. Jawabannya adalah', a - b)
            print('===' * 15)
    else :
        print('Jawaban tidak valid, hanya menerima jawaban bilangan bulat.')
        print('===' * 15)

def mode_pengurangan_1(): # Function to trigger the sbstraction formula
    while True :
        global select_quiz
        global score
        print(quiz)
        print()
        print()
        select_quiz = input('Masukkan jenis kuis: ')
        print('===' * 15)
        if select_quiz.isnumeric():
            if int(select_quiz) == 1 : 
                while True:
                    rumus_kurang()
            
            elif int(select_quiz) == 2 :
                score = 0
                for quiz_5 in range (1,6):
                    print('Pertanyaan ke', quiz_5, ': ', end='' )
                    rumus_kurang()
                print('Score kamu : ', score)
                print('===' * 15)
                score = 0
                continue

            elif int(select_quiz) == 3:
                intro()

            elif int(select_quiz) == 4:
                print('Terima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                quit()
            else : 
                print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
                print('===' * 15)
                continue
        else :
            print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
            print('===' * 15)
            continue

def rumus_campur(): # Random either + or - formula
    global score
    global select_quiz
    acak = random.randint(1,2)
    if acak == 1 :
        rumus_jumlah()

    elif acak == 2 :
        rumus_kurang()

def mode_campur(): # Trigger the random mode function
    while True : 
        global select_quiz
        global score
        print(quiz)
        print()
        print()
        select_quiz = input('Masukkan jenis kuis: ')
        print('===' * 15)
        if select_quiz.isnumeric():
            if int(select_quiz) == 1:
                while True :
                    rumus_campur()          
            elif int(select_quiz) == 2 :
                score = 0
                for aaa in range(1,6):
                    print('Pertanyaan ke', aaa, ": ", end='')
                    rumus_campur()
                print('Score kamu : ', score)
                print('===' * 15)
                score = 0
                continue
            elif int(select_quiz) == 3:
                intro()
            elif int(select_quiz) == 4 :
                print('Terima kasih telah bermain kuis ini. Sampai jumpa lagi!')
                quit()
            else : 
                print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
                print('===' * 15)
                continue
        else : 
            print('Program tidak mengenali perintah yang dimasukkan.\nSilakan memilih dari perintah yang tersedia.')
            print('===' * 15)
            continue
intro() # Start the program with intro function