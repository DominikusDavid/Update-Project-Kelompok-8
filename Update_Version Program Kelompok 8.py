# Kamus
# total_balance : int  # Saldo total pengguna
# topup_amount : int  # Jumlah uang yang ditambahkan ke saldo
# price_per_share : int  # Harga per lembar saham
# quantity_to_buy : int  # Jumlah lembar saham yang ingin dibeli
# total_cost : int  # Total biaya pembelian saham
# num_stocks : int  # Jumlah perusahaan IPO yang ditambahkan
# index : int  # Indeks dari kode saham dalam daftar
# sale_amount : int  # Total uang yang diperoleh dari penjualan saham
# seller_choice : int  # Pilihan menu untuk penjual
# home : str  # Menu utama
# home_input : str  # Input pilihan dari pengguna di menu utama
# user_id : str  # ID pengguna (username)
# user_name : str  # Nama lengkap pengguna
# user_choice : str  # Pilihan menu dari pengguna setelah login
# stock_code : str  # Kode saham yang ingin dibeli atau dijual
# dashboard : str  # Menu dashboard untuk pengguna setelah login
# dashboard_seller : str  # Menu dashboard untuk penjual
# stock_code_to_sell : str  # Kode saham yang ingin dijual
# valid_id : bool  # Menyatakan apakah ID pengguna valid atau tidak
# stock_codes : list[str]  # Daftar kode saham yang tersedia
# possible_ids : list[str]  # Daftar ID pengguna yang mungkin
# stock_prices : list[int]  # Daftar harga saham yang tersedia
# stock_quantities : list[int]  # Daftar jumlah lembar saham yang dimiliki
# buyer_portfolio : list[int]  # Portofolio pembeli yang berisi jumlah lembar saham yang dimiliki

# Codingan
total_balance = 0  # Saldo total pengguna
stock_codes = []  # Daftar kode saham
stock_prices = []  # Daftar harga saham
stock_quantities = []  # Daftar jumlah lembar saham yang dibeli
buyer_portfolio = []  # Portofolio pembeli
users = {}  # Menyimpan data pengguna dengan username sebagai kunci

def registrasi():
    global users  # Menyatakan bahwa kita menggunakan variabel global
    while True:
        print("=== Registrasi Pengguna ===")

        # Input Nama Lengkap
        full_name = input("Masukkan Nama Lengkap: ")
        
        # Input Username
        username = input("Masukkan Username: ")
        
        # Cek apakah username sudah ada
        if username in users:
            print("Username sudah terdaftar. Silakan pilih username lain.")
            continue
        
        # Input Umur
        while True:
            try:
                age = int(input("Masukkan Umur Anda: "))
                if age < 18:
                    print("Umur harus di atas 18 tahun. Silakan masukkan umur yang valid.")
                else:
                    break  # Keluar dari loop jika umur valid
            except ValueError:
                print("Input tidak valid! Harap masukkan angka untuk umur.")
        
        # Input Tipe Akun
        jenis_akun = input("Masukkan Tipe Akun (umum/sekuritas): ").lower()
        while jenis_akun not in ['umum', 'sekuritas']:
            print("Tipe akun tidak valid. Silakan masukkan umum atau sekuritas.")
            jenis_akun = input("Masukkan Tipe Akun (umum/sekuritas): ").lower()
        
        # Input Password
        password = input("Masukkan Password: ")
        
        # Simpan data pengguna
        users[username] = {
            'password': password,
            'type': jenis_akun,
            'full_name': full_name,
            'age': age
        }
        
        # Menampilkan data yang telah dimasukkan
        print("\n=== Data Registrasi ===")
        print(f"Username: {username}")
        print(f"Nama Lengkap: {full_name}")
        print(f"Umur: {age}")
        print(f"Tipe Akun: {jenis_akun}")
        
        # Tanya pengguna apakah ingin mendaftar lagi
        lagi = input("\nApakah Anda ingin mendaftar lagi? (ya/tidak): ").lower()
        if lagi != 'ya':
            print("Terima kasih telah mendaftar!")
            break

def login():
    global users  # Menyatakan bahwa kita menggunakan variabel global
    while True:
        print("=== Login Pengguna ===")
        
        # Meminta input Username
        username = input("Masukkan Username: ")  # Minta pengguna memasukkan username
        
        # Memeriksa apakah username ada
        if username not in users:
            print("Username tidak ditemukan. Silakan coba lagi.")
            continue
        
        # Meminta password
        password = input("Masukkan Password: ")

        # Memeriksa apakah password cocok
        if users[username]['password'] == password:
            user_type = users[username]['type']  # Mendapatkan tipe akun
            print(f"\nWelcome back {username} sebagai {user_type}")  # Menyapa pengguna
            return username, user_type  # Kembalikan username dan tipe akun
        else:
            print("Password salah. Silakan coba lagi.")

def main():
    global total_balance  # Menyatakan bahwa kita menggunakan variabel global
    global stock_quantities  # Menyatakan bahwa kita menggunakan variabel global
    while True:
        print("\n=== Menu Utama ===\n"
              "1. Registrasi\n"
              "2. Login\n"
              "3. Keluar\n")
        home_input = input("Pilih opsi (1/2/3): ")
        
        if home_input == "1":
            registrasi()
        elif home_input == "2":
            username, user_type = login()  # Panggil fungsi login dan simpan username dan tipe akun
            if username:  # Jika login berhasil
                # Definisikan dashboard di sini
                dashboard = str("Dashboard\n"
                                "Pilih salah satu\n"
                                "1. Topup\n"
                                "2. Pembelian\n"
                                "3. Penjualan\n"
                                "4. Lihat Portofolio\n"
                                "5. Logout")
                
                if user_type == 'umum':
                    user_choice = input(dashboard + "\nPilih Menu: ")  # Meminta pilihan menu dari pengguna

                    while user_choice != "5":  # Selama pengguna tidak memilih untuk logout
                        if user_choice == "1":
                            # Pro ses topup saldo
                            try:
                                topup_amount = int(input("Input Jumlah Topup: "))  # Minta jumlah topup
                                while topup_amount < 10000000:  # Validasi jumlah topup
                                    print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                                    topup_amount = int(input("Input Jumlah Topup: "))  # Minta input ulang jika invalid
                                total_balance += topup_amount  # Tambahkan jumlah topup ke saldo
                                
                                print(f"\nSaldo Akhir: {total_balance}\n")  # Tampilkan saldo akhir
                            except ValueError:
                                print("Input tidak valid! Harap masukkan angka.")
                            user_choice = input(dashboard + "\nPilih Menu: ")  # Minta pilihan menu

                        elif user_choice == "2":
                            # Proses pembelian saham
                            if not stock_codes:  # Cek jika tidak ada saham yang tersedia
                                print("Tidak ada saham yang tersedia untuk dibeli.")
                                user_choice = input(dashboard + "\nPilih Menu: ")
                                
                            else:
                                print("\nDaftar Kode Saham yang Tersedia:")  # Tampilkan daftar kode saham
                                for i in range(len(stock_codes)):
                                    print(f"{stock_codes[i]}: {stock_prices[i]} per lembar")  # Tampilkan kode dan harga saham
                                
                                stock_code = input("\nInput Kode Saham yang ingin dibeli (awalan $): ")  # Minta kode saham yang ingin dibeli
                                
                                if stock_code in stock_codes:  # Cek apakah kode saham valid
                                    index = stock_codes.index(stock_code)  # Dapatkan indeks kode saham
                                    price_per_share = stock_prices[index]  # Ambil harga saham berdasarkan kode
                                    print(f"Harga per lembar untuk {stock_code} adalah {price_per_share}")
                                    
                                    try:
                                        quantity_to_buy = int(input("Jumlah Lembar yang ingin dibeli: "))  # Minta jumlah lembar untuk dibeli
                                        total_cost = quantity_to_buy * price_per_share  # Hitung total biaya pembelian
                                        
                                        if total_cost > total_balance:  # Cek apakah saldo cukup
                                            print("Saldo tidak cukup untuk melakukan pembelian!")
                                        else:
                                            # Update saldo dan jumlah lembar saham yang dibeli
                                            total_balance -= total_cost
                                            stock_quantities[index] += quantity_to_buy  # Update jumlah lembar saham yang dibeli
                                            
                                            print(f"Pembelian berhasil! Sisa Saldo: {total_balance}")  # Konfirmasi pembelian
                                            user_choice = input(dashboard + "\nPilih Menu: ")  # Minta pilihan menu
                                    except ValueError:
                                        print("Input tidak valid! Harap masukkan angka.")
                                else:
                                    print("Kode saham tidak tersedia. Coba lagi.")  # Pesan jika kode saham tidak valid
                        
                        elif user_choice == "3":
                            # Proses penjualan saham
                            print("\nDaftar Kode Saham yang Tersedia untuk Dijual:")  # Tampilkan daftar kode saham
                            has_stocks = False  # Flag untuk mengecek apakah pengguna memiliki saham
                            for i in range(len(stock_codes)):
                                if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                                    print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")  # Tampilkan kode dan jumlah lembar
                                    has_stocks = True  # Set flag jika ada saham yang dimiliki
                            
                            if not has_stocks:  # Jika tidak ada saham yang dimiliki
                                print("Anda tidak memiliki apapun.")  # Tampilkan pesan
                            else:
                                stock_code_to_sell = input("\nMasukkan kode saham yang ingin dijual (awalan $): ")  # Minta kode saham yang ingin dijual
                                if stock_code_to_sell in stock_codes:  # Cek apakah kode saham valid
                                    index = stock_codes.index(stock_code_to_sell)  # Dapatkan indeks kode saham
                                    if stock_quantities[index] > 0:  # Cek apakah pengguna memiliki saham ini
                                        try:
                                            quantity_to_sell = int(input("Jumlah Lembar yang ingin dijual: "))  # Minta jumlah lembar untuk dijual
                                            if quantity_to_sell <= stock_quantities[index]:  # Cek apakah jumlah yang ingin dijual valid
                                                sale_amount = quantity_to_sell * stock_prices[index]  # Hitung total penjualan
                                                total_balance += sale_amount  # Tambahkan hasil penjualan ke saldo
                                                stock_quantities[index] -= quantity_to_sell  # Kurangi jumlah lembar yang dijual
                                                print(f"\nPenjualan berhasil! Sisa Saldo: {total_balance}")  # Konfirmasi penjualan
                                                print(f"\nJumlah lembar saham {stock_code_to_sell} yang tersisa: {stock_quantities[index]}")  # Tampilkan sisa lembar
                                            else:
                                                print("Jumlah yang ingin dijual melebihi jumlah yang dimiliki.")  # Pesan jika jumlah tidak valid
                                        except ValueError:
                                            print("Input tidak valid! Harap masukkan angka.")
                                    else:
                                        print("Anda tidak memiliki saham ini.")  # Pesan jika tidak memiliki saham
                                else:
                                    print("Kode saham tidak tersedia. Coba lagi.")  # Pesan jika kode saham tidak valid

                            # Minta pilihan menu setelah penjualan
                            user_choice = input(dashboard + "\nPilih Menu: ")  # Minta pilihan menu
                        
                        elif user_choice == "4":
                            # Menampilkan portofolio akhir
                            print("\nPortofolio Anda:")  # Tampilkan header portofolio
                            print(f"Saldo Anda: {total_balance}")  # Tampilkan saldo pengguna
                            if all(q == 0 for q in stock_quantities):  # Cek jika tidak ada saham yang dimiliki
                                print("Anda tidak memiliki apapun.")  # Tampilkan pesan jika tidak ada saham
                            else:
                                for i in range(len(stock_codes)):
                                    if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                                        print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")  # Tampilkan kode dan jumlah lembar
                            user_choice = input(dashboard + "\nPilih Menu: ")  # Minta pilihan menu

                        elif user_choice == "5":
                            # Keluar dari program
                            print("Terima kasih! Sampai jumpa lagi.")
                            break  # Keluar dari program

                elif user_type == 'sekuritas':
                    # Input untuk menambahkan perusahaan IPO
                    num_stocks = int(input("Masukkan jumlah perusahaan IPO: "))  # Minta jumlah perusahaan IPO
                    for i in range(num_stocks):
                        stock_code = input("Masukkan Kode Perusahaan (awalan $): ")  # Minta kode perusahaan
                        while not stock_code.startswith("$"):  # Validasi awalan kode
                            print("Masukkan kode perusahaan dengan awalan $")  # Pesan jika tidak valid
                            stock_code = input("Masukkan Kode Perusahaan (awalan $): ")
                        while True:
                            try:
                                stock_price = int(input("Masukkan Harga Perusahaan: "))  # Minta harga perusahaan
                                break  # Keluar dari loop jika input valid
                            except ValueError:
                                print("Input tidak valid! Harap masukkan angka.")
                        stock_codes.append(stock_code)  # Tambahkan kode saham ke daftar
                        stock_prices.append(stock_price)  # Tambahkan harga saham ke daftar
                        stock_quantities.append(0)  # Tambahkan 0 saham ke daftar, karena tidak ada saham yang ditambahkan
                    print("Perusahaan IPO berhasil ditambahkan.")

        elif home_input == "3":
            print("Terima kasih! Sampai jumpa lagi.")
            break  # Keluar dari program

if __name__ == "__main__":
    main()  # Jalankan fungsi utama