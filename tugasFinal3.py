class InputData:
    def __init__(self, value):
        self.value = {
            "sku" : value,
            "namaBarang" : namaBarang,
            "hargaSatuan" : hargaSatuan,
            "jmlStok": jmlStok,
        }
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = InputData(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value['sku'] == temp.value['sku']:
                return False
            if new_node.value['sku'] < temp.value['sku']:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value['sku']:
                temp = temp.left
            elif value > temp.value['sku']:
                temp = temp.right
            else:
                return True, temp.value
        return False,temp


# LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


# sorting
def bubble_sort(my_list):
  for i in range(len(my_list) - 1, 0, -1):
    for j in range(i):
      if my_list[j]['subTotal'] < my_list[j+1]['subTotal']:
        temp = my_list[j]
        my_list[j] = my_list[j+1]
        my_list[j+1] = temp
  return my_list

# function 1.1) Input Data Stok Barang
def menuSatuSatu():
    global namaBarang, hargaSatuan, jmlStok
    print("\n\n=================================")
    print("Halaman Input Data Stok Barang")
    print("=================================")
    noSku = input("Input 4 digit No. SKU : ")
    if len(noSku) == 4:
        try:
            int(noSku)
            hasil = myTree.contains(noSku)
            if hasil[0] == True:
                print("No. SKU yang anda inputkan sudah ada")
            else:
                print("=================================")
                namaBarang = input("input nama barang : ")
                while True:
                    try:
                        hargaSatuan = int(input("input harga : "))
                        jmlStok = int(input("input jumlah stok : "))
                        print("=================================")
                        myTree.insert(noSku)
                        print("berhasil disimpan")
                        print("=================================")
                        break
                    except ValueError:
                        print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")
                        print("=================================")
        except ValueError:
            print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")
    else:
        print("No. SKU yang anda inputkan tidak terdiri dari 4 digit angka")

def cekBarang():
    while True:
        pilihanUser = input("Apakah anda ingin melihat cek detail barang terlebih dahulu(Y/N)? ")
        if pilihanUser == 'Y':
                while True:
                    print("=================================")
                    inputSku = input("Silahkan input No. sku : ")
                    print("=================================")
                    if len(inputSku) == 4:
                        try:
                            int(inputSku)
                            hasil = myTree.contains(inputSku)
                            if hasil[0] == True:
                                print("\n\n==============================================")
                                print("Berikut adalah data barang : ")
                                print("==============================================")
                                print("No. SKU :", hasil[1]['sku'])
                                print("Nama Barang :", hasil[1]['namaBarang'])
                                print("Harga Satuan :", hasil[1]['hargaSatuan'])
                                print("Jumlah Stok :", hasil[1]['jmlStok'])
                                break                  
                            else:
                                print("No. SKU yang anda inputkan belum tersimpan")
                                print("Silahkan melakukan input data stok barang terlebih dahulu")
                                return False
                        except ValueError:
                            print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")
                    else:
                        print("No. SKU yang anda inputkan tidak terdiri dari 4 digit angka")
                    
        elif pilihanUser == 'N':
            return True
        elif pilihanUser == 'y' or pilihanUser == 'n':
            print("Silahkan input dengan huruf kapital sesuai pilihan yang tersedia")
        else:
            print("Inputan tersebut tidak ada dalam pilihan")

# function 1.2) Restok Barang
def menuSatuDua():
    print("\n\n=================================")
    print("Halaman Restok Barang")
    print("=================================")
    returnCekBarang = cekBarang()
    if returnCekBarang == True:
        while True:
            print("\n\n=================================")
            print("Silahkan melanjutkan restok barang")
            inputSku = input("Silahkan input No. sku : ")
            print("=================================")
            if len(inputSku) == 4:
                try:
                    int(inputSku)
                    hasil = myTree.contains(inputSku)
                    if hasil[0] == True:
                        print("\n\n==============================================")
                        print("Nama Barang :", hasil[1]['namaBarang'])
                        print("Harga Satuan :", hasil[1]['hargaSatuan'])
                        print("Jumlah Stok :", hasil[1]['jmlStok'])
                        print("==============================================")

                        while True:
                            try:
                                stokBaru = int(input("Input stok baru : "))
                                hasil[1]['jmlStok'] = hasil[1]['jmlStok'] + stokBaru
                                print("Jumlah total stok barang adalah : ", hasil[1]['jmlStok'])
                                print("==============================================")
                                print("Berhasil Diupdate")
                                print("==============================================")
                                break
                            except ValueError:
                                print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")                  
                    else:
                        print("No. SKU yang anda inputkan belum tersimpan")
                        print("Silahkan melakukan input data stok barang terlebih dahulu")
                    break
                except ValueError:
                    print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")
            else:
                print("No. SKU yang anda inputkan tidak terdiri dari 4 digit angka")
        
# function 2.1) Input Data Transaksi Baru
def menuDuaSatu():
    print("\n\n==============================================")
    print("Halaman Input Data Transaksi Baru")
    print("==============================================")
    returnCekBarang = cekBarang()
    if returnCekBarang == True:
        print("\n\n==============================================")
        print("Silahkan melanjutkan input data transaksi baru")
        print("==============================================")
        namaKonsumen = input("Input nama konsumen : ")
        def cekSku():
            while True:
                noSkuBarang = input("Input nomor SKU barang yang dibeli : ")
                if len(noSkuBarang) == 4:
                    try:
                        int(noSkuBarang)
                        def cekStok():
                            hasil = myTree.contains(noSkuBarang)
                            if hasil[0] == True:
                                while True:
                                    try:
                                        print("Stok barang saat ini : ", hasil[1]['jmlStok'])
                                        jumlahBeli = int(input("Input Jumlah Beli : "))
                                        subTotal = hasil[1]['hargaSatuan'] * jumlahBeli
                                        if hasil[1]['jmlStok'] >= jumlahBeli:
                                            hasil[1]['jmlStok'] = hasil[1]['jmlStok'] - jumlahBeli
                                            print("Stok barang setelah pembelian : ", hasil[1]['jmlStok'])
                                            transaksi = {
                                                'namaKonsumen' : namaKonsumen,
                                                'noSkuBarang' : noSkuBarang,
                                                'jumlahBeli' : jumlahBeli,
                                                'subTotal' : subTotal
                                            }
                                            if myLinkedList.get(0).value == None:
                                                myLinkedList.pop()
                                            myLinkedList.append(transaksi)
                                            print("==============================================")
                                            print("Data Transaksi Konsumen Berhasil Diinputkan")
                                            print("==============================================")
                                            while True:
                                                pilihanUser = input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ")
                                                if pilihanUser == 'Y':
                                                    cekSku()
                                                    break
                                                elif pilihanUser == 'N':
                                                    break
                                                elif pilihanUser == 'y' or pilihanUser == 'n':
                                                    print("Silahkan input dengan huruf kapital sesuai pilihan yang tersedia")
                                                else:
                                                    print("Inputan tersebut tidak ada dalam pilihan")
                                        elif hasil[1]['jmlStok'] < jumlahBeli:
                                            print("Jumlah Stok No. SKU yang Anda beli tidak mencukupi")
                                            while True:
                                                pilihanUser = input("Apakah ingin melanjutkan transaksi (Y/N)? ")
                                                if pilihanUser == 'Y':
                                                    cekStok()
                                                    break
                                                elif pilihanUser == 'N':
                                                    break
                                                elif pilihanUser == 'y' or pilihanUser == 'n':
                                                    print("Silahkan input dengan huruf kapital sesuai pilihan yang tersedia")
                                                else:
                                                    print("Inputan tersebut tidak ada dalam pilihan") 
                                        break
                                    except ValueError:
                                        print("Anda tidak hanya menginputkan angka\nSilakan hanya inputkan angka")                                            
                            else:
                                print("==============================================")
                                print("No. SKU yang diinputkan belum terdaftar")
                                print("==============================================")
                                while True:
                                    pilihanUser = input("Apakan ingin melanjutkan transaksi (Y/N)? ")
                                    if pilihanUser == 'Y':
                                        cekSku()
                                        break
                                    elif pilihanUser == 'N':
                                        break
                                    elif pilihanUser == 'y' or pilihanUser == 'n':
                                        print("Silahkan input dengan huruf kapital sesuai pilihan yang tersedia")
                                    else:
                                        print("Inputan tersebut tidak ada dalam pilihan")
                        cekStok()
                        break
                    except ValueError:
                        print("Anda tidak menginputkan 4 digit angka")              
                else:
                    print("No. SKU yang anda inputkan tidak terdiri dari 4 digit angka")          
        cekSku()

# function 2.2) Lihat Data Seluruh Transaksi Konsumen
def menuDuaDua():
        if myLinkedList.get(0).value == None:
            print("Data Transaksi Konsumen belum ada")
        else:
            returnCekBarang = cekBarang()
            if returnCekBarang == True:
                print("\n\n=================================")
                print("Data Seluruh Transaksi Konsumen")
                print("=================================")
                for x in range(myLinkedList.length):
                    tampilan = myLinkedList.get(x).value
                    print(x + 1, ") Nama Konsumen :", tampilan["namaKonsumen"])
                    print("    No. SKU barang yang dibeli :", tampilan["noSkuBarang"])
                    print("    Jumlah Beli :", tampilan["jumlahBeli"])
                    print("    Subtotal :", tampilan["subTotal"], "\n")

# function 2.3) Lihat Data Transaksi Berdasarkan Subtotal
def menuDuaTiga():
    if myLinkedList.get(0).value == None:
        print("Data Transaksi belum ada")
    else:
        returnCekBarang = cekBarang()
        if returnCekBarang == True:
            bubble = []
            print("\n\n=================================")
            print("Data Transaksi Berdasarkan Subtotal")
            print("=================================")
            for x in range(myLinkedList.length):
                bubble.append(myLinkedList.get(x).value)
            bubble_sort(bubble)
            for x in range(len(bubble_sort(bubble))):
                tampilan = bubble_sort(bubble)[x]
                print(x + 1,") Nama Konsumen :", tampilan["namaKonsumen"])
                print("    No. SKU barang yang dibeli :", tampilan["noSkuBarang"])
                print("    Jumlah Beli :", tampilan["jumlahBeli"])
                print("    Subtotal :", tampilan["subTotal"], "\n")

# Menu Utama
myTree = BinarySearchTree()
myLinkedList = LinkedList(None)
while True:
    print("\n\n=====================================")
    print("------Selamat Datang di SITORSI------")
    print("Sistem Informasi Stok dan Transaksi")
    print("=====================================")
    print("1) Kelola Stok Barang")
    print("2) Kelola Transaksi Konsumen")
    print("0) Exit Program")
    print("=================================")
    menuUtama = input("Input Pilihan : ")
    print("=================================")
    if menuUtama == "1":
        while True:
            print("\n\n=================================")
            print("   Sub Menu Kelola Stok Barang")
            print("=================================")
            print("1) Input Data Stok Barang")
            print("2) Restok Barang")
            print("0) kembali")
            print("=================================")
            menuSatu = input("Input Pilihan : ")
            print("=================================")
            if menuSatu == "1":
                menuSatuSatu()
            elif menuSatu == "2":
                menuSatuDua()
            elif menuSatu == "0":
                break
            else:
                print("Inputan tersebut tidak ada dalam pilihan menu")
    elif menuUtama == "2":
        while True:
            print("\n\n==============================================")
            print("     Sub Menu Kelola Transaksi Konsumen")
            print("==============================================")
            print("1) Input Data Transaksi Baru")
            print("2) Lihat Data Seluruh Transaksi Konsumen")
            print("3) Lihat Data Transaksi Berdasarkan Subtotal")
            print("0) kembali")
            print("==============================================")
            menuDua = input("Input Pilihan : ")
            print("==============================================")
            if menuDua == "1":
                menuDuaSatu()   
            elif menuDua == "2":
                menuDuaDua()         
            elif menuDua == "3":
                menuDuaTiga()
            elif menuDua == "0":
                break
            else:
                print("Angka yang anda input tidak ada dalam menu")
    elif menuUtama == "0":
        break
    else:
        print("Inputan tersebut tidak ada dalam pilihan menu")

print("=================================")
print("          Terima Kasih")
print("=================================")