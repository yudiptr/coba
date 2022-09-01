import string # Import string for punctuations
import html_functions # Import html_func.py
print('''Program untuk membuat word cloud dari text file
---------------------------------------------
hasilnya disimpan sebagai file html,
yang bisa ditampilkan di browser.


''')

stop = list()
stopwords = open('stopwords.txt', 'rt')
stop_log = stopwords.readlines()
for i in stop_log : # Put the stopwords into a list
    stop.append(i.replace('\n',''))
stopwords.close()

name_file = input('Silakan masukan nama file : ')
log = open(name_file, "r")
log_file = log.readlines() # Read the input file
temp_log_file = list()
early_data = {}

for i in log_file : # Put every words from text into a list
    j = i.split()
    for k in j :
        if k[-1] in string.punctuation and k[0] in string.punctuation:
            temp_log_file.append(k.lower().replace('\n','')[1:-1])
        elif k[-1] in string.punctuation:
            temp_log_file.append(k.lower().replace('\n','')[0:-1])
        elif k[0] in string.punctuation:
            temp_log_file.append(k.lower().replace('\n','')[1:])
        else : 
            temp_log_file.append(k.lower().replace('\n',''))
            
final_log = list()
def remove(): # Function to remove words if it's included in stopwords
    for word in temp_log_file:
        if word not in stop:
            final_log.append(word)
remove() # Run the remove function     

clean_list = list()
for comp in final_log: # Make word list without any punctuation
    clean_list.append(comp.strip(string.punctuation))

for name_list in clean_list: # Get how many words appear in file input
    result = clean_list.count(name_list)
    early_data[name_list] = result # Make dictionary for words : count

fixed_56 = dict()
# Sort the dict based on value and alphabetically
sorted_alphabet = dict(sorted(early_data.items(), key=lambda item: (item[1], item[0]), reverse=True)) 
value_56 = list(sorted_alphabet)[0:56] # Take the biggest 56 value from sorted one

for get_val in value_56: # Make a new dictionary for sorted biggset-alphabetically first 56 : value
    fixed_value = sorted_alphabet.get(get_val)
    fixed_56[get_val] = fixed_value
sorted_56 = sorted(value_56) # Sort from the biggest 56 alphabetically

min_val = fixed_56.get(value_56[55]) # Get the highest n lowest word which appear
max_val = fixed_56.get(value_56[0]) 
html_1 = ''

# Make html file form imported one (html_functions.py)
for a in sorted_56: 
    html_1 +=  " " + html_functions.make_HTML_word(a, fixed_56.get(a), int(max_val), int(min_val))
    
box = html_functions.make_HTML_box(html_1)
html_functions.print_HTML_file(box, name_file)


print('\n' + '\n' + '\n' + name_file, ':' +'\n')
print('''56 kata diurutkan berdasarkan jumlah kemunculan dalam pasangan
(jumlah:kata)\n\n\n''')
space = list()
for max_space in range (len(sorted_56)): # Format space for printing in console
    space.append(len(sorted_56[max_space - 1]))

len_console = 1
name = list(fixed_56)
for name in name[0:56]: # Print in console with format new line every 4 index
    if len_console == 4:  
        print(f'{fixed_56.get(name):>2}:{name}')
        print()
        len_console = 0
    else:
        print(f'{fixed_56.get(name):>2}:{name:<{max(space) + 4}}', end='')

    len_console += 1
log.close() # Close the opened file
input('\n\n\n' + 'Tekan Enter untuk keluar... ')