class User() :
    def __init__(self, user_name, tipe):
        """
        Constructor untuk class User
        """
        self.__user_name = user_name
        self.__tipe = tipe

    def get_name(self) : 
        return self.__user_name

    def get_tipe(self) : 
        return self.__tipe

class Seller(User) : 
    def __init__(self, user_name, tipe, pemasukan=0):
        """
        Constructor untuk class Seller
        """
        User.__init__(user_name, tipe)
        self.__pemasukan = 0
        self.list_barang_jual = []

    def get_pemasukan(self) : 
        return self.__pemasukan

    def set_pemasukan(self, pendapatan) : 
        self.__pemasukan += pendapatan

    def tambah_product(self, product_nama, price, stock) :
        self.list_barang_jual.append(Product(product_nama, int(price), int(stock), self.get_name()))
        list_product.append(Product(product_nama, int(price), int(stock), self.get_name()))

    def lihat_produk_jualan_saya(self) : 
        print("\nBerikut merupakan barang jualan saya")
        print("-------------------------------------")
        print("  Nama Product  |   Harga   | Stock ")
        print("-------------------------------------")
        for p in sorted(self.list_barang_jual) : 
            print(f"{p.get_name():^16s} | {p.get_price():^11d} | {p.get_stock():^7d}")
        print("-------------------------------------\n")

    def menu(self) : 
        print(f"Selamat datang {self.get_name()}")
        print("berikut menu yang bisa Anda lakukan:")
        print("1. TAMBAHKAN_PRODUK\n2. LIHAT_DAFTAR_PRODUK_SAYA\n3. LOG_OUT\n")
        print(f"Pemasukan anda {self.get_pemasukan()},")
        pilihan = input("Apa yang ingin Anda lakukan? ")

        if pilihan == "1":
            input_product = input("Masukkan data produk : ")
            input_product = input_product.split()
            check = get_product(input_product[0])
            if check == None:
                self.tambah_product(input_product[0], int(input_product[1]), int(input_product[2]))
            else :
                print("Produk sudah pernah terdaftar.")
            self.menu()
            
        if pilihan == "2":
            self.lihat_produk_jualan_saya()
            self.menu()

        elif pilihan == "3":
            print(f"Anda telah keluar dari akun {self.get_name()}")
            main()

class Buyer(User) : 
    def __init__(self, user_name, saldo, tipe):
        super().__init__(user_name, tipe)
        self.__saldo = saldo
        self.list_barang_beli = []

    def beli(self, penjual, harga, produk):
        self.__saldo -= harga
        penjual.set_pemasukan(int(harga))
        for ele in penjual.list_barang_jual:
            if ele.get_name() == produk.get_name():
                ele.set_stock() 
        produk.set_stock()

    def menu(self):
        print(f"Selamat datang {self.get_name()},\nberikut menu yang bisa Anda lakukan:\n1. LIHAT_SEMUA_PRODUK\n2. BELI_PRODUK\n3. RIWAYAT_PEMBELIAN_SAYA\n4. LOG_OUT\n")
        print(f"Saldo anda {self.__saldo},")
        pilihan = input("Apa yang ingin anda lakukan? ")

        if pilihan == '1':
            print("------------------------------------------------\n  Nama Product  |   Harga   | Stock |  Penjual\n------------------------------------------------")
            for p in list_product:
                print(f"{p.get_name():^16s}|{p.get_price():^11d}|{p.get_stock():^7d}|{p.get_seller():^10s}")

            self.menu()
        if pilihan == '2':
            beli = input("Masukkan barang yang ingin dibeli : ")
            temp_var = "variabel sementara"
            for p in list_product:
                for s in list_user:
                    if p.get_name() == beli and int(self.__saldo) >= int(p.get_price()) and int(p.get_stock()) > 0 and s.get_name() == p.get_seller():
                        print(f"Berhasil membeli {beli} dari {p.get_seller()}")
                        
                        self.beli(s, p.get_price(), p)
                        self.list_barang_beli.append((beli, p.get_price(), p.get_seller()))
                        temp_var = "sudah beli"

                    elif p.get_name() == beli and int(p.get_stock()) <= 0:
                        print("Maaf, stok produk telah habis")

                    elif p.get_name() == beli and int(self.__saldo) < int(p.get_price()):
                        print(f'Maaf, saldo Anda tidak cukup untuk membeli {beli}].')
            
            if temp_var != 'sudah beli':
                print(f"Barang dengan nama {beli} tidak ditemukan dalam Dekdepedia.")

            self.menu()

        if pilihan == "3":
            print("Berikut merupakan barang yang saya beli\n----------------------------------------\n Nama Produk   |   Harga   |  Penjual\n----------------------------------------")
            for p, harga, penjual in sorted(self.list_barang_beli):
                print(f"{p:<16s}|{harga:<11d}|{penjual:<10s}")
            print("----------------------------------------")

            self.menu()

        if pilihan == '4':
            print(f"Anda telah keluar dari akun {self.get_name()}")
            main()

class Product() : 
    def __init__(self, name, price, stock, seller):
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__seller = seller
    
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock
    def get_seller(self):
        return self.__seller

    def set_stock(self):
        self.__stock = self.__stock - 1
        return self.__stock

    def __lt__(self, other):
        a = self.get_name()
        b = other.get_name()
        return a < b

def get_user(name, list_user):
    """
    Method untuk mengembalikan user dengan user_name sesuai parameter
    """
    for user in list_user:
        if user.get_name() == name:
            return user
    return None

def get_product(name):
    """
    Method untuk mengembalikan product dengan name sesuai parameter
    """
    for product in list_product:
        if product.get_name() == name:
            return product
    return None

list_user = []
list_product = []
validator = '''!()[]{};:'"\,<>./?@#$%^&*~'''
def main():
    print("Selamat datang di Dekdepedia!")
    print("Silakan memilih salah satu menu di bawah:")
    print("1. Sign Up")
    print("2. Log In")
    print("3. Exit")

    pilih = input("Pilihan Anda: ")

    if pilih == "1" : 
        banyak_user = input("Jumlah akun yang ingin didaftarkan : ")

        print("Data akun: ")
        if banyak_user.isnumeric():
            if int(banyak_user)>0:

                for i in range(int(banyak_user)): 
                    data_user = input(str(i+1)+". ")
                    for a in validator:
                        if a in data_user:
                            print('Akun tidak Valid:')
                            break
                    data_user_list = data_user.split()
                    check = get_user(data_user_list[1], list_user)
                    if len(data_user_list):
                        if check == None:
                            if data_user_list[0] + ' ' == "SELLER " and len(data_user_list) == 2:
                                list_user.append(Seller(user_name=data_user_list[1], tipe="SELLER"))

                            elif data_user_list[0] + ' ' == "BUYER " and len(data_user_list) == 3:
                                list_user.append(Buyer(user_name=data_user_list[1], saldo=int(data_user_list[2]), tipe="BUYER"))
                            else:
                                print("Akun tidak valid.")
                        else : 
                            print("Username sudah terdaftar.")
                    else :
                        print('Perintah tidak valid.')
            else :
                print('Perintah tidak valid.')
        else:
            print('Perintah tidak valid.')
        print()
        main()

    elif pilih == "2" : 
        user_name_login = input("user_name : ")
        user_logged_in = get_user(user_name_login, list_user)
        if user_logged_in == None:
            print(f"Akun dengan username {user_name_login} tidak ditemukan")
            main()
        
        print(f"Anda telah masuk dalam akun {user_name_login} sebagai {user_logged_in.get_tipe()}")
        user_logged_in.menu()

    elif (pilih == "3") : 
        print("Terima kasih telah menggunakan Dekdepedia!")
        exit(0)
main()