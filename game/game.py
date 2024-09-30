import random 

welcome_massages = "WELLCOME IN CHIKO GAMES!"
chiko_position = random.randint (1, 10)

print("====***********************====")
print(f"** {welcome_massages} **")
print("====***********************====")

nama_user = input("siapa nama kamu?: ")
print(f"Hallo! selamat datang {nama_user} di GAME chiko!")

print(f'''
      Hallo! {nama_user} Coba perhatikan ruangan di bawah ini!
      |_| |_| |_| |_| |_| |_| |_| |_| |_| |_|
      ''')
print("Ruangan tersebut adalah tempat chiko bersembunyi!")

pilihan_user = int(input("Menurutmu CHIKO ada di ruangan nomor berapa? [1/2/3/4/5/6/7/8/9/10?: "))
konfirmasi_user = input(f"Apakah kamu yakin memilih nomor {pilihan_user}?: ")
if konfirmasi_user : "Y"
                        
if pilihan_user == chiko_position:
    print(f"YEAY! SELAMAT {nama_user} MENANG, KARENA CHIKO BERADA DI {chiko_position} DAN PILIHANMU ADALAH {pilihan_user}")
else:
    print(f'''YAHH! SAYANG SEKALI {nama_user} KALAH! KARENA JAWABANMU SALAH!
          JAWABANMU {pilihan_user}, SEDANGKAN CHIKO BERADA DI RUANGAN NOMOR {chiko_position}''')