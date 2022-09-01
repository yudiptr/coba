input_name = input('Masukkan nama file input: ') # Askin input file 
output_name = input('Masukkan nama file output: ') # Askin output file
try : # Check wether file is exist or not
    name_in = open(input_name, "r") 
except IOError: # If file doesn't exist, run this
    print('File input tidak ada :(')
    print('Program selesai. Tekan enter untuk keluar...', end='')
    input()
else : # If file exist, run this
    name_in = open(input_name, "r") # Open the file
    hastag = 0 # Set variable to be acumulated
    mention = 0
    url = 0

    inpot = name_in.readlines() # Read the input file for every sentence
    if inpot == []: # Making exception for file exist but zonk
        print('File input ada tapi kosong :(')
        print('Program selesai. Tekan enter untuk keluar...', end='')
        input()
    else : 
        name_out = open(output_name, "w") # Write the output file, auto clear if file do exist before

        for lst in  range (len(inpot)): # Iterate every line
            single_sentence = inpot[lst].split(' ') # Split every line per word
            for new_sentece in single_sentence: # Iterate the word for each line
                if new_sentece == '': # In case first sentence is empty but other line's not
                    print(new_sentece, end=' ', file = name_out)
                # Manipulate input as the agreement
                elif (new_sentece[0] == '@') :
                    print('(M)',end=' ', file = name_out)
                    mention += 1
                elif (new_sentece[0] == '#') :
                    print('(H)',end=' ', file = name_out)
                    hastag += 1
                elif (new_sentece[0:4] == 'www.'):
                    print('(U)',end=' ', file = name_out)
                    url += 1
                else :
                    if '\n' in new_sentece:
                        slash = new_sentece.find('\n')
                        print(new_sentece[0:slash], end=' ', file = name_out)
                    else:
                        print(new_sentece, end=' ', file = name_out)
            print(' ', file = name_out) # to move to new sentence in txt file

        print(' ', file = name_out)
        print('#' * 15, file = name_out)
        # Print the variable
        print(f"Mention :{mention:>6}", file = name_out)
        print(f"Hastag  :{hastag:>6}", file = name_out)
        print(f"Url     :{url:>6}", file = name_out)
        # Close file
        name_in.close()
        name_out.close()
        print('Output berhasil ditulis pada ' + output_name )
        print('Program selesai. Tekan enter untuk keluar...', end='')
        input()
