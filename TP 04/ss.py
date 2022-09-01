from tkinter import *
from tkinter import messagebox

class EAN13:
    def __init__(self, master):
        self.master = master
        self.name_var = StringVar()
        self.code_var = StringVar()

        master.title('EAN-13 Barcode Maker')

        name = Label(master, text = 'Save bardcode to PS file [eg: EAN13.eps]:', \
            font = 'arial 10 bold').pack()

        master.geometry('400x450')

        input_name = Entry(master, width = 25, textvariable=self.name_var)

        input_name.pack()

        code = Label(master, text = 'Enter code (first 12 decimal digits):', \
            font = 'arial 10 bold').pack()

        input_code = Entry(master, width = 25, textvariable=self.code_var)

        input_code.pack()
        self.temp_data = ''
        self.new_lay = Label(master, text=self.temp_data)
        self.new_lay.pack()
        self.canvas = Canvas(master, width = 330, height = 330, bg = "white")
        master.bind('<Return>', self.check_code)
        self.canvas.pack()
        
    def check_code(self, event):
        punc = ''' /\:*?"<>| '''
        self.canvas.delete("all")
        counter = 0
        if (len(self.code_var.get()) == 12) and (self.name_var.get()[-4:] == '.eps'):
            for a in punc:
                if a in self.name_var.get()[0:-4]:
                    counter += 1
            if not counter :
                if self.code_var.get().isnumeric():
                    counter = 0
                    for a in range(12):
                        for b in (self.code_var.get()[a]):
                            if (a+1) % 2 == 0 :
                                counter += (int(b)*3)
                            else:
                                counter += int(b)
                    self.last_digit = ''
                    self.temp_data = str(self.code_var.get())
                    if counter % 10 == 0 :
                        self.temp_data += '0'
                        self.last_digit = '0'
                    else :
                        b = counter % 10
                        self.temp_data += str(10 - b)
                        self.last_digit = str(10 - b)

                    self.data_new = self.temp_data[:]
                    self.fixed_digit = []
                    ## Masukin tiap digit ke list dalem list, linya diiterasi
                    for a in self.temp_data:
                        self.fixed_digit.append(a)
                    self.new_lay["text"] = self.temp_data
                    sample = self.temp_data[0]
                    if sample == '0':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = l_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = l_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = l_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = l_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = l_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '1':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = l_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = l_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = g_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = g_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '2':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = l_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = g_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = l_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = g_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '3':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = l_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = g_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = g_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = l_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '4':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = l_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = l_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = g_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = g_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '5':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = l_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = l_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = g_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '6':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = g_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = l_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = l_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '7':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = l_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = g_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = l_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = g_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '8':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = l_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = g_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = g_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = l_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    elif sample == '9':
                        self.fixed_digit[1] = l_code[self.fixed_digit[1]]
                        self.fixed_digit[2] = g_code[self.fixed_digit[2]]
                        self.fixed_digit[3] = g_code[self.fixed_digit[3]]
                        self.fixed_digit[4] = l_code[self.fixed_digit[4]]
                        self.fixed_digit[5] = g_code[self.fixed_digit[5]]
                        self.fixed_digit[6] = l_code[self.fixed_digit[6]]
                        self.fixed_digit[7] = r_code[self.fixed_digit[7]]
                        self.fixed_digit[8] = r_code[self.fixed_digit[8]]
                        self.fixed_digit[9] = r_code[self.fixed_digit[9]]
                        self.fixed_digit[10] = r_code[self.fixed_digit[10]]
                        self.fixed_digit[11] = r_code[self.fixed_digit[11]]
                        self.fixed_digit[12] = r_code[self.fixed_digit[12]]
                    self.temp_data = ''.join(self.fixed_digit)
                    self.creat_canvas(self.temp_data)
                    self.last_digit = ''
                    self.data_new = ''
                    self.fixed_digit.clear()
                    self.temp_data = ''
                    self.canvas.postscript(file=self.name_var.get(), colormode='color')
                else :
                    messagebox.showerror('Wrong input!', 'Please enter correct input.')
            else :
                    messagebox.showerror('Wrong input!', 'Please enter correct input.')
        else:
            messagebox.showerror('Wrong input!', 'Please enter correct input.')

    def creat_canvas(self, lst):
        self.canvas.create_text(180,80, font = 'arial 15 bold', text = 'EAN-13 Barcode: ')
        self.canvas.create_line(30,100,30,200, width=3, fill='blue')
        self.canvas.create_line(33,100,33,200, width=3, fill='white')
        self.canvas.create_line(36,100,36,200, width=3, fill='blue')
        self.canvas.pack()
        x = 39
        for a in range(1,len(lst)):
            b = lst[a]
            if a == 43:
                self.canvas.create_line(x,100,x,200, width=3, fill ='white')
                self.canvas.create_line(x+3,100,x+3,200, width=3, fill='blue')
                self.canvas.create_line(x+6,100,x+6,200, width=3, fill ='white')
                self.canvas.create_line(x+9,100,x+9,200, width=3, fill='blue')
                self.canvas.create_line(x+12,100,x+12,200, width=3, fill ='white')
                x += 15
            elif b == '1':
                self.canvas.create_line(x,100,x,180, width=3, fill='green')
                x += 3
            elif b == '0' :
                self.canvas.create_line(x,100,x,180, width=3, fill = 'white')
                x += 3
        self.canvas.create_line(x,100,x,200, width=3, fill='blue')
        self.canvas.create_line(x+3,100,x+3,200, width=3, fill='white')
        self.canvas.create_line(x+6,100,x+6,200, width=3, fill='blue')
        self.canvas.create_text(20,210, font = 'arial 15 bold', text = self.data_new[0])
        form_x1 = 50
        for a in range(1,7):
            self.canvas.create_text(form_x1,210, font = 'arial 15 bold', text = self.data_new[a])
            form_x1 += 20
        form_x2 = 188
        for a in range(7,13):
            self.canvas.create_text(form_x2,210, font = 'arial 15 bold', text = self.data_new[a])
            form_x2 += 20
        self.canvas.create_text(165,240,fill='red', font = 'arial 15 bold', text = f"Check Digit : {self.last_digit}")
        
def main():
    root = Tk()
    new_root = EAN13(root)
    root.mainloop()

l_code = {'0':'0001101', '1':'0011001', '2':'0010011', '3':'0111101', '4':'0100011', '5':'0110001', '6':'0101111', '7':'0111011', '8':'0110111', '9':'0001011'}
g_code = {'0':'0100111', '1':'0110011', '2':'0011011', '3':'0100001', '4':'0011101', '5':'0111001', '6':'0000101', '7':'0010001', '8':'0001001', '9':'0010111'}
r_code = {'0':'1110010', '1':'1100110', '2':'1101100', '3':'1000010', '4':'1011100', '5':'1001110', '6':'1010000', '7':'1000100', '8':'1001000', '9':'1110100'}

if __name__ == "__main__":
    main()