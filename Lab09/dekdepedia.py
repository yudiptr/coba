class User() : # Set class parent *user
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.user_name = user_name
        self.tipe = tipe

    def get_name(self) :  # Find the name of the username
        return self.user_name

    def get_tipe(self) :  # Find the type of the username
        return self.tipe

class Seller(User) : # Child class for seller
    def __init__(self, user_name, tipe): 
        """
        Constructor untuk class Seller
        """
        self.user_name = user_name
        self.list_barang_jual = []
        self.pemasukan = 0
        self.tipe = tipe

    def intro(self) : # If the user logged in into seller, it will run first
        print(f'Anda telah masuk dalam akun {self.user_name} sebagai {self.tipe}')
        print(f'''Selamat datang {self.user_name},\nberikut menu yang bisa Anda lakukan:
1. TAMBAHKAN_PRODUK\n2. LIHAT_DAFTAR_PRODUK_SAYA\n3. LOG_OUT''')
        self.menu() # Run the menu Seller.menu_function
    
    def get_pemasukan(self) : # To get the pemasukan
        return self.pemasukan

    def set_pemasukan(self, cuan): # To update pemasukkan seller
        self.pemasukan += int(cuan)
        return self.pemasukan

    def tambah_product(self, item, harga, stock):
        if (harga.isnumeric()) and (stock.isnumeric()): # Check the harga and stock isnumeric or not
            if (int(harga) >= 0) and (int(stock) > 0): # Find the possible amount of stock and possible price
                self.list_barang_jual.append([item, harga, stock]) # update seller sell.list
                nama_barang = Product(item, int(harga), int(stock), self.get_name()) # Register the item into class product
                list_product.append(nama_barang) # Add the product object
            else :
                print('Perintah tidak valid.')
        else :
            print('Perintah tidak valid.')

    def lihat_produk_jualan_saya(self) : # To print the seller on sale item
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        for product in sorted(self.list_barang_jual): # Make it into sorted alphabetically, price, and amount
            print(f"{product[0]:^16}|{product[1]:^9}|{product[2]:^6}")
        print("-------------------------------------\n")

    def menu(self): # Func to ask what command the user want to input
        print(f"\nPemasukan anda {self.get_pemasukan()},")
        ask = input("Apa yang ingin Anda lakukan? ")
        if ask == '1':
            command = input('Masukkan data produk : ')
            command_split = command.split() 
            if len(command_split) == 3 :
                check_product = get_product(command_split[0])
                if check_product == None:
                    self.tambah_product(command_split[0], command_split[1], command_split[2])
                else : 
                    print(f"Product {command_split[0]} sudah ada dalam Dekdepedia\nMasukkan product lain :D")
            else :
                print('Perintah tidak valid.')
            self.menu()
        elif ask == '2':
            self.lihat_produk_jualan_saya()
            self.menu()
        elif ask == '3':
            self.log_out()
            main()
        else: # Validating input
            print('Perintah tidak valid.')
            self.menu()

    def log_out(self): # To define the log out and back into main menu
        print(f"Anda telah keluar dari akun {self.user_name}")
        main()

class Buyer(User) : # Child class for buyer type
    def __init__(self, user_name, tipe, saldo):
        """
        Constructor untuk class Buyer
        """
        self.user_name = user_name
        self.tipe = tipe
        self.saldo = int(saldo)
        self.list_barang_beli = []

    def get_saldo(self): # To get saldo from user.buyer
        return self.saldo

    def list_item(self): # To print what items are on the sale list in sorted form
        temp_data = []
        print("\nBerikut merupakan daftar produk di Dekdepedia")
        print("-----------------------------------------------")
        print("  Nama Produk   |   Harga   | Stock |  Penjual ")
        print("-----------------------------------------------")
        for product in list_product : # Get the product name, price, stock, and seller by using class product attribute
            temp_data.append([product.get_name(), product.get_harga(), product.get_stock(), product.get_seller()])
        for a in sorted(temp_data): # Sorthing them based on name, price, stock, and seller
            print(f'{a[0] :^16}|{a[1] :^11}|{a[2]:^7}|{a[3]:^11}')
        print("-------------------------------------\n")   
    
    def set_saldo(self, beli) : #To update saldo buyer
        self.saldo -= int(beli)
        return self.saldo

    def intro(self): # When the user logged in into buyer, it will run first
        print(f"Anda telah masuk dalam akun {self.get_name()} sebagai BUYER")
        print(f'''\nSelamat datang {self.get_name()},\nberikut menu yang bisa Anda lakukan:
1. LIHAT_SEMUA_PRODUK\n2. BELI_PRODUK\n3. RIWAYAT_PEMBELIAN_SAYA\n4. LOG_OUT''')
        self.menu()

    def menu(self): # Ask the command from buyer
        print(f"\nSaldo anda {self.get_saldo()},")
        command = input("Apa yang ingin Anda lakukan? ")
        # Ask the command and run this menu again till the user want to log out
        if (command == "1") :
            self.list_item()
            self.menu()

        elif (command == "2") :
            self.buy()
            self.menu()

        elif (command == "3") :
            self.riwayat()
            self.menu()
        
        elif (command == "4") :
            self.log_out()
        else: # Validating command
            print('Perintah tidak valid.')
            self.menu()
    
    def buy(self): # Function when tue buyer want to buy
        ask = input("Masukkan barang yang ingin dibeli : ")
        check = get_product(ask) # Check the item is on the list or not
        if check == None: # 
            print(f"Barang dengan nama {ask} tidak ditemukan dalam Dekdepedia.")
        else : # If the item on list -> run this
            if check.get_stock() > 0: # Validating the stock, price, and buyer wallet
                if check.get_harga() <= self.get_saldo(): 
                    print(f"Berhasil membeli {check.get_name()} dari {check.get_seller()}")
                    self.set_saldo(check.get_harga())
                    seller = check.get_seller()
                    for a in list_user:
                        b = a.get_name()
                        if b == seller:
                            a.set_pemasukan(check.get_harga()) # Update seller income
                            check.set_stock() # Update the stock
                            self.list_barang_beli.append([check.get_name(), check.get_harga(), a.get_name()])
                            for c in a.list_barang_jual:
                                if ask in c: # Update the stock for the seller
                                    c[2] = str(int(c[2])- 1)

                elif check.get_harga() > self.get_saldo():
                    print(f"Maaf, saldo Anda tidak cukup untuk membeli {check.get_name()}.")
                elif check.get_stock() == 0 :
                    print(f"Maaf, stok produk {check.get_name()} telah habis.")
            else :
                print(f"Maaf, stok produk {check.get_name()} telah habis.")

    def log_out(self): # To log out from buyer account and back to main menu
        print(f"Anda telah keluar dari akun {self.user_name}")
        main()

    def riwayat(self): # Print buyer buy history in sorted alphabet, price, amount form 
        print("Berikut merupakan barang yang saya beli")
        print("-------------------------------------")
        print("  Nama Produk  |   Harga   | Penjual ")
        print("-------------------------------------")
        for product in sorted(self.list_barang_beli) :
            print(f"{product[0]:^16}|{product[1]:^11}|{product[2]:^11}")
        print(f"-------------------------------------\n")

class Product():
    def __init__(self, user_name, harga, stock, seller): # Constructor for class product
        self.user_name = user_name
        self.harga = int(harga)
        self.stock = int(stock)
        self.seller = seller

    def get_name(self): # Get the item name
        return self.user_name
    
    def get_harga(self): # Get the item price
        return self.harga

    def get_stock(self): # Get the item stock
        return self.stock

    def get_seller(self): # Get the seller
        return self.seller

    def set_stock(self): # Update stock
        self.stock -= 1
        return self.stock

def get_user(name): # To check wether the user is registered or not
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name): # To check wether the product is already on the list or not
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

list_user = [] # To containing the obj of user
list_product = [] # To containing the obj of product
punc = '''!()[]{};:'"\,<>./?@#$%^&*~'''

def main(): # Define function main menu:
    print("Selamat datang di Dekdepedia!")
    print("Silakan memilih salah satu menu di bawah:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    pilih = input("Pilihan Anda: ")
    print()

    # Validating input
    if pilih == "1" : 
        sign_up()

    elif pilih == "2": 
        log_in()

    elif pilih == "3" : 
        print("Terima kasih telah menggunakan Dekdepedia!")
        exit()
    else :
        print('Perintah tidak valid.')
    print()
    main()
    
def sign_up(): # To define func if user want to log in
    banyak_user = input("Jumlah akun yang ingin didaftarkan : ")
    if banyak_user.isnumeric(): # Validating the amount is numeric and > 0
        if int(banyak_user) > 0:
            print("Data akun: ")
            for i in range (int(banyak_user)) : 
                data_user = input(str(i+1)+". ")
                counter = 0
                for stop in punc: # Validating the user format
                    if counter == 0:
                        if stop in data_user:
                            print('Akun tidak valid.')
                            counter += 1
                            continue
                data_split = data_user.split()
                if len(data_split): # Validating if user is input anything
                    if (data_split[0] + ' ' == 'BUYER ') and (len(data_split) == 3):
                        if data_split[2].strip('-').isnumeric(): # Make sure the saldo of registered buyer is int and >= 0
                            if int(data_split[2]) >= 0:
                                check_data = get_user(data_split[1]) #  Check wether the user is already registered or not   
                                if check_data == None:
                                    data_split[1] = Buyer(data_split[1], data_split[0], data_split[2])
                                    list_user.append(data_split[1]) # Add obj of this username into list_user
                                else :
                                    print(f"Username {data_split[1]} sudah terdaftar.")
                            else :
                                print('Akun tidak valid.')
                        else :
                            print('Akun tidak valid.')

                    elif (data_split[0] + ' ' == 'SELLER ') and (len(data_split) == 2):
                        check_data = get_user(data_split[1]) # Check the user is already registered or not
                        if check_data == None:           
                            data_split[1] = Seller(data_split[1], data_split[0])
                            list_user.append(data_split[1]) # Append the obj of this username into list_user
                        else : 
                            print(f"Username {data_split[1]} sudah terdaftar.")
                    else :
                        print('Akun tidak valid.')
                else : 
                    print('Akun tidak valid.')
        else :
            print('Perintah tidak valid.')
    else :
        print('Perintah tidak valid.')

def log_in():
    user_name_login = input("\nuser_name : ")
    check_data = get_user(user_name_login) # Validating the user
    if check_data == None :
        print(f'Akun dengan username {user_name_login} tidak ditemukan')
    else : # If user is registered on list, it will run intro based on its class buyer or seller
        check_data.intro()
main()