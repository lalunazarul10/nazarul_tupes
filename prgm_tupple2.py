transaksi = []

def add_transaksi(transaksi_id, produk_id, quantity):
    if quantity > 0:
        transaksi.append((transaction_id, product_id, quantity))
    else:
        print("Jumlah harus lebih dari 0")

def get_transactions():
    return transaksi

# Contoh penggunaan
if __name__ == "__main__":
    transaction_id = 1
    while True:
        product_id = int(input("Masukkan ID produk (0 untuk keluar): "))
        if product_id == 0:
            break
        quantity = int(input("Masukkan jumlah: "))
        add_transaksi(transaction_id, product_id, quantity)
        transaction_id += 1
    
    for transaction in get_transactions():
        if transaction[2] > 3:
            print(f"Transaksi {transaksi[0]} memiliki jumlah besar: {transaction}")
        else:
            print(f"Transaksi {transaction[0]}: {transaction}")
