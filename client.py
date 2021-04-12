# import library socket karena akan menggunakan IPC socket
import socket
from blockchain import Blockchain
# definisikan tujuan IP server
ip = '127.0.0.1'
# definisikan port dari server yang akan terhubung
port = 12345
# definisikan ukuran buffer untuk mengirimkan pesan
SIZE = 1024
# definisikan pesan yang akan disampaikan
print('pesan yang ingin anda kirim ke server : ')
pesan = input('')
# buat socket tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((ip, port))
# kirim pesan ke server
s.send(pesan.encode())
# terima pesan dari server
pesanServer = s.recv(SIZE).decode()
# tampilkan pesan atau repty dari server
print('pesan dari server : ' + str(pesanServer))
#tutup koneksi
s.close()
