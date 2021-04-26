import hashlib
import time
import os
import threading

def hash_file():
	lock.acquire()
	filename=input("File name: ")
	with open(filename, 'rb') as file:
		data = file.read()
		n= hashlib.md5(data).hexdigest()
	print ('Hash file: ')
	print(n)
	print(os.getppid())

	lock.acquire()
	lock.release()
	print("lock")
	lock.release()

def lock_rlock():
	t1 = threading.Thread(target = hash_file)
	t2 = threading.Thread(target = hash_file)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

lock = threading.Lock()
lock_rlock()
