
#Kamus1
# total_balance, topup_amount, price_per_share, quantity_to_buy, total_cost, num_stocks, index, sale_amount, seller_choice : int
# home, home_input, user_id, user_name, user_choice, stock_code, dashboard, dashboard_seller, stock_code_to_sell : str            
# valid_id : bool
# stock_codes, possible_ids : list[str]
# stock_prices, stock_quantities, buyer_portfolio : list[int]

#Codingan
total_balance = 0  # Saldo total pengguna
stock_codes = []  # Daftar kode saham
stock_prices = []  # Daftar harga saham
stock_quantities = []  # Daftar jumlah lembar saham yang dibeli
buyer_portfolio = []  # Portofolio pembeli
possible_ids = ["#", "*", "%"]  # Daftar simbol yang valid untuk ID pengguna 

#Login page
home = str("\nSekuritas Ambalabu\n"
"1. Login\n"
"2. Tutup program\n")
print(home)
home_input = str(input("Pilih Opsi: "))
while(home_input != "2"):
    if home_input == "1":
        # Meminta input ID pengguna
        user_id = input("Masukkan ID Anda (contoh: #David): ")  # Minta pengguna memasukkan ID
        valid_id = False  # Variabel untuk memeriksa kevalidan ID

        # Memeriksa apakah ID valid
        while not valid_id:
            # Cek apakah ID mengandung simbol yang valid dan hanya satu simbol
            symbol_count = sum(1 for symbol in possible_ids if symbol in user_id)

            if symbol_count == 1:  # Hanya satu simbol yang diperbolehkan
                valid_id = True  # ID valid
            else:
                print("ID Invalid! Pastikan hanya menggunakan satu simbol (#, *, %) dan disertai nama.")
                user_id = input("Masukkan ID Anda (contoh: #David): ")  # Minta input ulang jika ID tidak valid

        user_name = user_id[1:]  # Mengambil nama pengguna setelah simbol

        print(f"\nWelcome back {user_name}")  # Menyapa pengguna


        # Memeriksa jenis pengguna berdasarkan ID
        if "#" in user_id: 
            # Dashboard untuk Pembeli
            dashboard = str("Dashboard Pembeli\n"
                            "Pilih salah satu\n"
                            "1. Topup\n"
                            "2. Pembelian\n"
                            "3. Lihat Portofolio\n"
                            "4. Logout")
            
            print(dashboard)  # Menampilkan dashboard pembeli
            user_choice = input("Pilih Menu: ")  # Meminta pilihan menu dari pengguna

            while user_choice != "4":  # Selama pengguna tidak memilih untuk logout
                if user_choice == "1":
                    # Proses topup saldo
                    topup_amount = int(input("Input Jumlah Topup: "))  # Minta jumlah topup
                    while topup_amount < 10000000:  # Validasi jumlah topup
                        print("Jumlah Invalid! Topup tidak bisa kurang dari 10 juta")
                        topup_amount = int(input("Input Jumlah Topup: "))  # Minta input ulang jika invalid
                    total_balance += topup_amount  # Tambahkan jumlah topup ke saldo
                
                    print(f"\nSaldo Akhir: {total_balance}\n")  # Tampilkan saldo akhir
                    print(dashboard)  # Tampilkan kembali dashboard
                    user_choice = input("Pilih Menu: ")  # Minta pilihan menu

                elif user_choice == "2":
                    # Proses pembelian saham
                    if not stock_codes:  # Cek jika tidak ada saham yang tersedia
                        print("Tidak ada saham yang tersedia untuk dibeli.")
                    else:
                        print("\nDaftar Kode Saham yang Tersedia:")  # Tampilkan daftar kode saham
                        for i in range(len(stock_codes)):
                            print(f"{stock_codes[i]}: {stock_prices[i]} per lembar")  # Tampilkan kode dan harga saham
                        
                        stock_code = input("\nInput Kode Saham yang ingin dibeli: ")  # Minta kode saham yang ingin dibeli
                        
                        if stock_code in stock_codes:  # Cek apakah kode saham valid
                            index = stock_codes.index(stock_code)  # Dapatkan indeks kode saham
                            price_per_share = stock_prices[index]  # Ambil harga saham berdasarkan kode
                            print(f"Harga per lembar untuk {stock_code} adalah {price_per_share}")
                            
                            quantity_to_buy = int(input("Jumlah Lembar yang ingin dibeli: "))  # Minta jumlah lembar untuk dibeli
                            total_cost = quantity_to_buy * price_per_share  # Hitung total biaya pembelian
                            
                            if total_cost > total_balance:  # Cek apakah saldo cukup
                                print("Saldo tidak cukup untuk melakukan pembelian!")
                            else:
                                # Update saldo dan jumlah lembar saham yang dibeli
                                total_balance -= total_cost
                                stock_quantities[index] += quantity_to_buy  # Update jumlah lembar saham yang dibeli
                                
                                print(f"Pembelian berhasil! Sisa Saldo: {total_balance}")  # Konfirmasi pembelian
                        else:
                            print("Kode saham tidak tersedia. Coba lagi.")  # Pesan jika kode saham tidak valid
                
                    print(dashboard)  # Tampilkan kembali dashboard
                    user_choice = input("Pilih Menu: ")  # Minta pilihan menu

                elif user_choice == "3":
                    # Menampilkan portofolio akhir
                    print("\nPortofolio Akhir:")  # Tampilkan header portofolio
                    for i in range(len(stock_codes)):
                        if stock_quantities[i] > 0:  # Hanya tampilkan saham yang dimiliki
                            print(f"{stock_codes[i]}: {stock_quantities[i]} lembar")  # Tampilkan kode dan jumlah lembar
                    print(f"\n{dashboard}")  # Tampilkan kembali dashboard
                    user_choice = input("Pilih Menu: ")  # Minta pilihan menu

            # Simpan portofolio pembeli untuk digunakan oleh penjual
            buyer_portfolio = stock_quantities.copy()  # Salin portofolio pembeli
            print(home)
            home_input = str(input("Input opsi: "))
        elif "*" in user_id:
            # Dashboard Penjual
            dashboard_seller = ("\nDashboard Penjual\n"
                                "Pilih salah satu\n"
                                "1. Penjualan\n"
                                "2. Portofolio\n"
                                "3. Logout")
            
            seller_choice = 0  # Inisialisasi pilihan penjual
            while seller_choice != 3:  # Selama pengguna tidak memilih untuk logout
                print(dashboard_seller)  # Tampilkan dashboard penjual
                seller_choice = int(input("Pilih salah satu: "))  # Minta pilihan menu dari penjual
                
                if seller_choice == 1:
                    # Menampilkan portofolio pembeli untuk penjual
                    print("\nPortofolio Pembeli:")  # Tampilkan header portofolio pembeli
                    for i in range(len(stock_codes)):
                        if buyer_portfolio[i] > 0:  # Hanya tampilkan saham yang dimiliki
                            print(f"{stock_codes[i]}: {buyer_portfolio[i]} lembar")  # Tampilkan kode dan jumlah lembar
                    
                    stock_code_to_sell = input("\nMasukkan kode saham yang ingin dijual: ")  # Minta kode saham yang ingin dijual
                    if stock_code_to_sell in stock_codes:  # Cek apakah kode saham valid
                        index = stock_codes.index(stock_code_to_sell)  # Dapatkan indeks kode saham
                        if buyer_portfolio[index] > 0:  # Cek apakah penjual memiliki saham ini
                            quantity_to_sell = int(input("Jumlah Lembar yang ingin dijual: "))  # Minta jumlah lembar untuk dijual
                            if quantity_to_sell <= buyer_portfolio[index]:  # Cek apakah jumlah yang ingin dijual valid
                                sale_amount = quantity_to_sell * stock_prices[index]  # Hitung total penjualan
                                total_balance += sale_amount  # Tambahkan hasil penjualan ke saldo
                                buyer_portfolio[index] -= quantity_to_sell  # Kurangi jumlah lembar yang dijual
                                print(f"\nPenjualan berhasil! Sisa Saldo: {total_balance}")  # Konfirmasi penjualan
                                print(f"\nJumlah lembar saham {stock_code_to_sell} yang tersisa: {buyer_portfolio[index]}")  # Tampilkan sisa lembar
                            else:
                                print("Jumlah yang ingin dijual melebihi jumlah yang dimiliki.")  # Pesan jika jumlah tidak valid
                        else:
                            print("Anda tidak memiliki saham ini.")  # Pesan jika tidak memiliki saham
                    else:
                        print("Kode saham tidak tersedia. Coba lagi.")  # Pesan jika kode saham tidak valid

                elif seller_choice == 2:
                    # Menampilkan portofolio penjual
                    print("\nPortofolio Anda:")  # Tampilkan header portofolio penjual
                    for i in range(len(stock_codes)):
                        if buyer_portfolio[i] > 0:  # Hanya tampilkan saham yang dimiliki
                            print(f"{stock_codes[i]}: {buyer_portfolio[i]} lembar")  # Tampilkan kode dan jumlah lembar
            print(home)
            home_input = str(input("Input opsi: "))

        elif "%" in user_id: 
            # Input untuk menambahkan perusahaan IPO
            num_stocks = int(input("Masukkan jumlah perusahaan IPO: "))  # Minta jumlah perusahaan IPO
            for i in range(num_stocks):
                stock_code = input("Masukkan Kode Perusahaan (awalan $): ")  # Minta kode perusahaan
                while not stock_code.startswith("$"):  # Validasi awalan kode
                    print("Masukkan kode perusahaan dengan awalan $")  # Pesan jika tidak valid
                    stock_code = input("Masukkan Kode Perusahaan (awalan $): ")  # Minta input ulang
                
                stock_codes.append(stock_code)  # Tambahkan kode saham ke daftar
                price_per_share = int(input(f"Harga saham per lembar untuk {stock_code}: "))  # Minta harga saham per lembar
                stock_prices.append(price_per_share)  # Tambahkan harga saham ke daftar
                stock_quantities.append(0)  # Inisialisasi jumlah lembar saham yang dibeli dengan 0

            print("\nPerusahaan IPO berhasil ditambahkan.\n")  # Konfirmasi penambahan perusahaan IPO
            print(home)
            home_input = str(input("Input Opsi: ")) #Setelah menambahkan perusahaan IPO, langsung kembali ke home screen
            
    else:
        while(home_input != "1"):
            print("Input Invalid!")
            home_input = str(input("Input Opsi: "))
            if (home_input == "2"):
                break
print("Terima kasih!")