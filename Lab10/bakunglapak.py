import tkinter as tk
import tkinter.messagebox as tkmsg

class Product(object): # Class for set the object of product
    def __init__(self, nama, harga, stok):
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok

    def get_nama(self):
        return self.__nama

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        self.__stok -= jumlah

class Buyer(object): # Class to set feature for the buyer
    def __init__(self):
        self.__daftar_beli = {}

    def add_daftar_beli(self, produk, jumlah): 
        if produk in self.__daftar_beli: # If buyer have alreade bought the item and wanna add more, value will be increased
          self.__daftar_beli[produk] += jumlah
        else : # If buyer haven't bought, it will add new dict
          self.__daftar_beli[produk] = jumlah

    def get_daftar_beli(self):
      return self.__daftar_beli

class WindowLihatBarang(tk.Toplevel):
    def __init__(self, product_dict, master = None):
        super().__init__(master)
        self.product_dict = product_dict
        self.wm_title("Daftar Barang")
        self.create_widgets()

    def create_widgets(self):
        self.lbl_judul = tk.Label(self, \
                                  text = 'Daftar Barang Yang Tersedia').grid(row = 0, column = 1)
        self.lbl_nama = tk.Label(self, \
                                 text = 'Nama Produk').grid(row = 1, column = 0)
        self.lbl_harga = tk.Label(self, \
                                  text = 'Harga').grid(row = 1, column = 1)
        self.lbl_stok = tk.Label(self, \
                                 text = 'Stok Produk').grid(row = 1, column = 2)
        i = 2
        for nama, barang in sorted(self.product_dict.items()): # Print the entire list on the market
            tk.Label(self, \
                     text = f"{nama}").grid(row = i, column= 0)
            tk.Label(self, \
                     text = f"{barang.get_harga()}").grid(row = i, column= 1)
            tk.Label(self, \
                     text = f"{barang.get_stok()}").grid(row = i, column= 2)
            i += 1

        self.btn_exit = tk.Button(self, text = "EXIT", \
                                  command = self.destroy).grid(row = i, column=1) # Make button to close pop up list market

class WindowBeliBarang(tk.Toplevel):
    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.wm_title("Beli Barang") # Make title of the app to be Beli Barang
        self.geometry("250x120") # Make the dimention of the app
        self.create_widgets()

    def create_widgets(self):
        self.nama_beli = tk.Label(self, text='Form Beli Barang').grid(row = 0, column= 2)
        self.ent_nama_barang = tk.StringVar() # Set container for name variable
        self.ent_jumlah = tk.StringVar() # Container for jumlah variable
        self.label_nama = tk.Label(self, text ='Nama Barang').grid(row = 1, column= 0)
        self.label_beli = tk.Label(self, text ='Jumlah').grid(row = 2, column= 0)
        self.form_nama = tk.Entry(self, textvariable=self.ent_nama_barang)
        self.form_nama.grid(row = 1, column= 2)
        self.form_beli = tk.Entry(self, textvariable=self.ent_jumlah)
        self.form_beli.grid(row = 2, column= 2)
        self.button_beli = tk.Button(self, text='Beli', command = self.beli_barang).grid(row = 3, column= 2) # Make button to buy the written input from user
        self.button_exit = tk.Button(self, text='Exit', command = self.destroy).grid(row = 4, column= 2) # Make button to close the buy pop up

    def beli_barang(self):
        nama_barang = self.ent_nama_barang.get()
        jumlah = self.ent_jumlah.get()
        if nama_barang == "": # Validating the input if the name is filled or not
            a = tkmsg.askretrycancel('Barang Not Found!','Nama barang tidak boleh kosong.')
            if not a: # If user click cancel, the buy pop up will close
                self.destroy()
        elif jumlah == '': # Validating the possible input for jumlah
            tkmsg.showerror('Jumlah Error!','Jumlah barang tidak boleh kosong.')
        elif jumlah.strip('-').isnumeric(): # Make sure the jumlah is make senses
            jumlah = int(jumlah)
            if jumlah > 0 :
                if nama_barang not in self.product_dict:  # Check wether the product is on the list or not
                    a = tkmsg.askretrycancel('Barang Not Found!', f"Barang dengan nama {nama_barang} tidak ditemukan dalam BakungLapak.")
                    if not a: # If user click cancel, pop up buy will be closed
                        self.destroy()
                elif self.product_dict[nama_barang].get_stok() == 0: 
                    tkmsg.showinfo('Stock Empty', 'Maaf, stock produk telah habis.')
                elif self.product_dict[nama_barang].get_stok() - jumlah < 0: # If the stock is lower than demand, pop up stock unavailable will appear
                    tkmsg.showinfo('Stock Unavailable!','Jumlah barang yang ada tidak mencukupi.')
                else :
                    barang = self.product_dict[nama_barang]
                    buyer.add_daftar_beli(barang, jumlah)
                    barang.set_stok(jumlah)
                    self.form_nama.delete(0, tk.END) # To clean the form of name of the product
                    self.form_beli.delete(0, tk.END) # To clean the form of value of the product
                    tkmsg.showinfo("Berhasil!", f"Berhasil membeli {nama_barang} sejumlah {jumlah}")
            elif jumlah == 0 :
               tkmsg.showerror('Jumlah Error!','Jumlah barang yang dibeli tidak boleh 0')
            else :
                tkmsg.showerror('Jumlah Error!','Jumlah barang yang dibeli tidak boleh dibawah 0')
        else : tkmsg.showerror('Buy Error', 'Harap masukkan jumlah yang valid.')

class WindowCheckOut(tk.Toplevel):
    def __init__(self, buyer, master = None):
        super().__init__(master)
        self.wm_title("Daftar Barang")
        self.daftar_dibeli = buyer.get_daftar_beli()
        self.create_widgets()

    def create_widgets(self):
        i = 2
        tk.Label(self, text = 'Kerangjangku').grid(row=0, column=1)
        tk.Label(self, text = 'Nama Produk').grid(row=1, column=0)
        tk.Label(self, text = 'Harga Barang').grid(row=1, column=1)
        tk.Label(self, text = 'Jumlah').grid(row=1, column=2)
        new_daftar = []
        for product in self.daftar_dibeli: # Make a list which include name, price, and value that had been bought
            new_daftar.append([product.get_nama(), product.get_harga(), self.daftar_dibeli[product]])
        if self.daftar_dibeli: # Validating if buyer had bought anything or not
            for nama in sorted(new_daftar): # If Yes: It will print the list on the pop up
                tk.Label(self, \
                        text = f"{nama[0]}").grid(row = i, column= 0)
                tk.Label(self, \
                        text = f"{nama[1]}").grid(row = i, column= 1)
                tk.Label(self, \
                        text = f"{nama[2]}").grid(row = i, column= 2)
                i += 1
        else : # If not: it will print this on the pop up
            tk.Label(self, text = 'Belum ada barang yang dibeli :(').grid(row=i, column=1)
            i += 1
        tk.Button(self , text = 'EXIT', command = self.destroy).grid(row = i+2, column=1) # Make the exit button

class MainWindow(tk.Frame):

    def __init__(self, buyer, product_dict, master = None):
        super().__init__(master)
        self.buyer = buyer
        self.product_dict = product_dict
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang di BakungLapak. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_barang = tk.Button(self, \
                                                 text = "LIHAT DAFTAR BARANG", \
                                                 command = self.popup_lihat_barang) # Make the button to ask the user 
                                                 # To see the market list
                                                 
        self.btn_beli_barang = tk.Button(self, \
                                         text = "BELI BARANG", \
                                         command = self.popup_beli_barang) # Make the button to ask the user 
                                         # To Buy the product

        self.btn_check_out = tk.Button(self, \
                                       text = "CHECK OUT", \
                                       command = self.popup_check_out) # Make the button to ask the user 
                                       # To check the summary list
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.master.destroy) # Make the button to ask the user 
                                  # To quit the app
        self.label.pack()
        self.btn_lihat_daftar_barang.pack()
        self.btn_beli_barang.pack()
        self.btn_check_out.pack()
        self.btn_exit.pack()

    # semua barang yand dijual
    def popup_lihat_barang(self):
        WindowLihatBarang(self.product_dict)

    # menu beli barang
    def popup_beli_barang(self):
        WindowBeliBarang(self.buyer, self.product_dict)

    # menu riwayat barang yang dibeli
    def popup_check_out(self):
        WindowCheckOut(self.buyer)

if __name__ == "__main__":
    buyer = Buyer()
    product_dict = {"Kebahagiaan" : Product("Kebahagiaan", 999999, 1),
                    "Kunci TP3 SDA" : Product("Kunci TP3 SDA", 1000000, 660),
                    "A" : Product("A", 3, 100), "B" : Product("B", 3, 100), }

    m = MainWindow(buyer, product_dict)
    m.master.title("BakungLapak")
    m.master.mainloop()